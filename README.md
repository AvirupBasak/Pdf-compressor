# 📄 PDF Compressor & PPTX to PDF Converter

A lightweight and user-friendly web application built using **Python, Flask, and standard web technologies**.

This application provides two useful document utilities:

- **PDF Compressor:** Compress PDF documents using selectable compression levels.
- **PPTX to PDF Converter:** Convert PowerPoint presentations (`.pptx`) into PDF format.

The application runs locally on your computer and uses **Ghostscript** for PDF compression and **LibreOffice** for PowerPoint conversion.

---

## 🌐 Live Frontend Demo

You can preview the user interface here:

👉 https://avirupbasak.github.io/Pdf-compressor/

⚠️ **Note:**

The live demo showcases only the frontend design. Backend functionality requires Python, Ghostscript, and LibreOffice installed on your computer.

The GitHub Pages demo and Flask application use separate entry-point files:

- `index.html` in the repository root: GitHub Pages frontend.
- `templates/index.html`: Flask application homepage.

Do not delete the root `index.html` if you want to preserve the GitHub Pages demo.

---

## 🚀 Features

### 📄 1. PDF Compressor

- Upload PDF files from your device.
- Choose between three compression levels:
  - **Minimum:** Best quality, least compression.
  - **Medium:** Balanced compression and quality.
  - **Maximum:** Strongest compression, smallest file size.
- Compress PDF documents using Ghostscript.
- Download compressed PDF files.
- Dedicated compression success page.

### 📊 2. PPTX to PDF Converter

- Upload PowerPoint presentations (`.pptx`).
- Convert presentations into PDF format using LibreOffice.
- Download converted PDF files.
- Automatically generate timestamp-based filenames (including seconds).
- Dedicated conversion success page.

### 🎨 3. User Interface

- Clean and responsive interface.
- Drag-and-drop file upload.
- Display selected filename and file size.
- Remove selected files before processing.
- Separate upload areas for PDF and PPTX files.
- Consistent success pages for both utilities.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | File selection and drag-and-drop |
| Ghostscript | PDF compression engine |
| LibreOffice | PPTX to PDF conversion |
| subprocess | External command execution |

---

## 📦 Installation & Setup

### System Requirements

Before running the application, make sure you have:

1. Python 3.x
2. Ghostscript
3. LibreOffice
4. Git (optional, for cloning the repository)

**Important:** Ghostscript and LibreOffice are external software dependencies. They are not installed through Python's `requirements.txt`.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AvirupBasak/Pdf-compressor.git
cd Pdf-compressor
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell):**

```powershell
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download and Install Ghostscript

Ghostscript is required for PDF compression.

You can download the installer from the project Google Drive folder:

👉 **[Download Ghostscript & LibreOffice Installers](https://drive.google.com/drive/folders/1RSIlwbOqEF4p4pXzdPY1BOqZoKnjzF8X?usp=sharing)**

Alternatively, download Ghostscript from its official website:

👉 https://www.ghostscript.com/download/gsdnld.html

After downloading, run the installer and complete the installation.

The application currently uses this Ghostscript executable path in `app.py`:

```python
r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe"
```

If your installed version or location is different, update the path in `app.py` accordingly.

### 5️⃣ Download and Install LibreOffice

LibreOffice is required for converting PowerPoint presentations into PDF format.

Download the installer from the project Google Drive folder:

👉 **[Download Ghostscript & LibreOffice Installers](https://drive.google.com/drive/folders/1RSIlwbOqEF4p4pXzdPY1BOqZoKnjzF8X?usp=sharing)**

Alternatively, use the official LibreOffice website:

👉 https://www.libreoffice.org/download/download-libreoffice/

Run the installer and complete the installation.

The application looks for LibreOffice through the system PATH. If it cannot find it, it uses this Windows fallback path:

```python
r"C:\Program Files\LibreOffice\program\soffice.exe"
```

If your installation is located elsewhere, update the path in `app.py`.

### 6️⃣ Run the application

After installing all the required dependencies, run:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

You can now use both PDF Compressor and PPTX to PDF Converter.

---

## 📂 Project Structure

```text
Pdf-compressor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── compressor.html
│   └── converter.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
├── compressed/
├── converted/
│
└── .gitignore
```

---

## ⚙️ How It Works

### PDF Compression Workflow

1. User uploads a PDF document.
2. Flask receives and stores the uploaded file.
3. User selects a compression level.
4. Ghostscript processes the PDF.
5. The compressed PDF is saved in the `compressed/` directory.
6. A success page provides the download option.

### PPTX Conversion Workflow

1. User uploads a PowerPoint presentation.
2. Flask generates a timestamp-based filename.
3. The uploaded PPTX is temporarily stored in the `uploads/` directory.
4. LibreOffice converts the presentation into PDF format.
5. The converted PDF is saved in the `converted/` directory.
6. The original uploaded PPTX is deleted after processing.
7. A success page provides the converted PDF download option.

---

## ⚠️ Important Notes

- The `uploads`, `compressed`, and `converted` directories are created automatically during runtime.
- Ghostscript is required for PDF compression.
- LibreOffice is required for PPTX-to-PDF conversion.
- Both external applications must be installed separately.
- Python dependencies and their versions are listed in `requirements.txt`.
- Converted PDF filenames include the current date and time down to seconds.
- The current application configuration uses Windows-specific executable paths.
- This application is currently designed for local use.

---

## 🎯 Future Improvements

- Standalone EXE packaging.
- Compression preview statistics.
- Automatic cleanup of generated files.
- Improved error handling.
- Additional document conversion formats.
- More PDF manipulation utilities.

---

## 👨‍💻 Author

**Avirup Basak**

BCA Student | Aspiring To Create Something New

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Thanks for checking out the project!