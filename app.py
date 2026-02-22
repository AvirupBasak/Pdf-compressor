# From the Flask library, bring these three tools. Where Flask Creates the web server, render_template loads html files and request Receives data from browser. 
from flask import Flask, render_template, request, send_file

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

# Defensive folder creation (suto creates \uploads and \compressed folder)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)


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



# "@app" This is a route decorator. When browser visits /, run the function below.
@app.route("/")
def home():
    return render_template("index.html")


# Only accept POST requests at /compress route.
@app.route("/compress", methods=["POST"])


# This function runs when form is submitted.
def compress():

    # Reads uploaded file. This name must match HTML:<input type="file" name="pdf_file">. ("request.files" Contains uploaded files only.)
    pdf_file = request.files["pdf_file"]

    # Reads normal form data. Matches HTML:<select name="mode">
    mode = request.form["mode"]

    # Gets original file name:
    filename = pdf_file.filename

    # Creates full path: uploads/example.pdf
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    output_path = os.path.join(app.config["COMPRESSED_FOLDER"], filename)


    # Physically saves the file to disk. Until this line → file exists only in memory. After this line → file exists in folder.
    pdf_file.save(input_path)

    # call the core logic of compression
    compress_pdf(input_path,output_path,mode)

    # retun a new page after file uploading and compression
    return f"""
        <h2>PDF compressed successfully ✅</h2>

        <p><b>Original file:</b> {filename}</p>
        <p><b>Compression mode:</b> {mode}</p>

        <br>

        <a href="/download/{filename}">
            ⬇ Download compressed PDF
        </a>

        <br><br>

        <a href="/">🔁 Compress another file</a>
    """ 

# New route for download the file on user browser
@app.route("/download/<filename>")

def download(filename):
    # finding the filename that is downloaded from the COMPRESSED_FOLDER
    file_path = os.path.join(app.config["COMPRESSED_FOLDER"], filename)

    # Flask, take this file from my computer and give it to the user.
    return send_file(file_path, as_attachment=True)


# Run server only when file is executed directly
if __name__ == "__main__":
    app.run(debug=True)