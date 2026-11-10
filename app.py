# From the Flask library, bring these three tools. Where Flask Creates the web server, render_template loads html files and request Receives data from browser. 
from flask import Flask, render_template, request, send_file

# for saving name
from datetime import datetime

# This imports are for pptx to pdf converter
from werkzeug.utils import secure_filename
import shutil

# importing operating system module for file paths, folder joining, cross-platform support. Example: "os.path.join("uploads", "file.pdf")" Works on Windows, Linux, Mac.
import os

# subprocess is a built-in Python module. It allows Python to: run external programs installed on your computer.
import subprocess

# Creating Flask application object on app variable.
app = Flask(__name__)

# It stores the folder name where PDFs will be saved
UPLOAD_FOLDER = "uploads"
COMPRESSED_FOLDER = "compressed"

# Stores that value inside Flask configuration. After that Flask can remember:UPLOAD_FOLDER → uploads
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["COMPRESSED_FOLDER"] = COMPRESSED_FOLDER

# Folder for PPTX to Pdf converter
CONVERTED_FOLDER = "converted"
app.config["CONVERTED_FOLDER"] = CONVERTED_FOLDER


# Defensive folder creation (suto creates \uploads and \compressed folder)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

# Defensive folder creation for pptx to pdf converter
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# main Compression logic start from here
def compress_pdf(input_path, output_path, mode):

    # making a dict for initialize the value for ghostscript understanding
    quality = {
        "min": "/prepress",
        "mid": "/ebook",
        "max": "/screen"
    }

    # making a list that will execute one by one internally on cmd
    gs_command = [
        r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe", #start the ghostscript software
        "-sDEVICE=pdfwrite", #Ghostscript, output should be a PDF.
        "-dCompatibilityLevel=1.4", #Create PDF version 1.4. Because:maximum compatibility, smaller file size, supports compression well. Newer versions are bigger.
        f"-dPDFSETTINGS={quality.get(mode, '/screen')}", #Ghostscript internally applies the comparission level
        "-dNOPAUSE", #no waiting
        "-dQUIET", #no console spam
        "-dBATCH", #auto exit
        f"-sOutputFile={output_path}", #Save result to the output path.
        input_path #The original PDF (first tell the program how to work, then tell it what to work on.)
    ]

    # Run this command exactly as written on the list gs_command.
    subprocess.run(gs_command, check=True)

def convert_pptx_to_pdf(input_path, output_folder):

    soffice = shutil.which("soffice")

    if not soffice:
        soffice = (
            r"C:\Program Files\LibreOffice\program\soffice.exe"
        )

    command = [
        soffice,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_folder,
        input_path
    ]

    subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        timeout=120
    )

    output_filename = (
        os.path.splitext(os.path.basename(input_path))[0] + ".pdf"
    )

    output_path = os.path.join(output_folder, output_filename)

    if not os.path.exists(output_path):
        raise RuntimeError("PDF conversion failed!")

    return output_path



# "@app" This is a route decorator. When browser visits /, run the function below.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/converter", methods=["GET"])
def converter():
    return render_template("converter.html")


@app.route("/compressor", methods=["GET"])
def compressor():
    return render_template("compressor.html")


# Only accept POST requests at /compress route.
@app.route("/compressor", methods=["POST"])
# This function runs when form is submitted.
def compress():
    # Reads uploaded file. This name must match HTML:<input type="file" name="pdf_file">. ("request.files" Contains uploaded files only.)
    pdf_file = request.files.get("pdf_file")

    if not pdf_file or not pdf_file.filename:
        return "Please upload a PDF file.", 400
    
    # Gets original file name:
    filename = secure_filename(pdf_file.filename)

    if not filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed.", 400

    

    # Reads normal form data. Matches HTML:<select name="mode">
    mode = request.form["mode"]


    # Creates full path: uploads/example.pdf
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    output_path = os.path.join(app.config["COMPRESSED_FOLDER"], filename)


    # Physically saves the file to disk. Until this line → file exists only in memory. After this line → file exists in folder.
    pdf_file.save(input_path)

    # call the core logic of compression
    compress_pdf(input_path,output_path,mode)

    # retun a new page after file uploading and compression
    
    return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PDF Compressed Successfully</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>

            <body>

                <main class="success-page">
                    <div class="success-card">

                        <div class="success-icon">✓</div>

                        <h2>PDF Compressed Successfully!</h2>
                        <p class="success-message">
                            Your PDF is ready to download.
                        </p>

                        <div class="file-details">
                            <div class="detail-row">
                                <span>Original file</span>
                                <strong>{filename}</strong>
                            </div>

                            <div class="detail-row">
                                <span>Compression mode</span>
                                <strong>{mode.upper()}</strong>
                            </div>
                        </div>

                        <a href="/download/{filename}" class="download-btn">
                            Download Compressed PDF
                        </a>

                        <a href="/compressor" class="another-btn">
                            Compress Another File
                        </a>

                        <a href="/" class="home-link">
                            ← Back to Home
                        </a>

                    </div>
                </main>

            </body>
            </html>
        """ 


# New route for download the pdf file on user browser
@app.route("/download-converted/<filename>")
def download_converted(filename):

    file_path = os.path.join(
        app.config["CONVERTED_FOLDER"],
        secure_filename(filename)
    )

    return send_file(
        file_path,
        as_attachment=True,
        download_name="converted.pdf"
    )


# New route for download the pdf file on user browser
@app.route("/download/<filename>")

def download(filename):
    # finding the filename that is downloaded from the COMPRESSED_FOLDER
    file_path = os.path.join(app.config["COMPRESSED_FOLDER"], filename)

    # Flask, take this file from my computer and give it to the user.
    return send_file(file_path, as_attachment=True)




# Only accept POST requests at /converter route.
@app.route("/converter", methods=["POST"])
def convert_pptx():

    pptx_file = request.files.get("pptx_file")

    if not pptx_file or not pptx_file.filename:
        return "Please upload a PowerPoint file.", 400

    filename = secure_filename(pptx_file.filename)

    if not filename.lower().endswith(".pptx"):
        return "Only PPTX files are allowed.", 400

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_name = f"{timestamp}_{filename}"

    input_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        unique_name
    )

    pptx_file.save(input_path)

    
    try:
        output_path = convert_pptx_to_pdf(
            input_path,
            app.config["CONVERTED_FOLDER"]
        )

        converted_filename = os.path.basename(output_path)

        return f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">

                    <title>PPTX Converted Successfully</title>

                    <link rel="stylesheet" href="/static/style.css">
                     </head>
                    <body>
                    <main class="success-page">
                        <div class="success-card">
                            <div class="success-icon">✓</div>
                            <h2>Conversion Successful!</h2>
                            <p class="success-message">
                                Your PowerPoint presentation is now a PDF.
                            </p>
                            <div class="file-details">

                                <div class="detail-row">
                                    <span>Original file</span>
                                    <strong>{filename}</strong>
                                </div>

                                <div class="detail-row">
                                    <span>Converted format</span>
                                    <strong>PDF (.pdf)</strong>
                                </div>

                            </div>

                            <a href="/download-converted/{converted_filename}"
                               class="download-btn">
                                Download Converted PDF
                            </a>

                            <a href="/converter" class="another-btn">
                                Convert Another File
                            </a>

                            <a href="/" class="home-link">
                                ← Back to Home
                            </a>

                        </div>
                    </main>

                </body>
                </html>
            """

    except (
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
            RuntimeError,
            OSError
        ):
            app.logger.exception("PPTX conversion failed")
            return "Conversion failed. Please check LibreOffice installation.", 500

    finally:
        if os.path.exists(input_path):
            os.remove(input_path)



# Run server only when file is executed directly
if __name__ == "__main__":
    app.run(debug=True)