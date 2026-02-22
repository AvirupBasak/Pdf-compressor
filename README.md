# 📄 PDF Compressor Web App

A simple and efficient web application to compress PDF files with selectable compression levels.
Built using **Flask**, **Ghostscript**, and standard web technologies, this tool allows users to upload a PDF, choose a compression mode, and download the optimized file instantly.

---

## 🚀 Features

* 📂 Upload any PDF file from your device
* ⚙️ Choose compression level:

  * **Minimum** — best quality, least compression
  * **Medium** — balanced compression
  * **Maximum** — strongest compression, smallest size
* ⬇️ Download the compressed PDF instantly
* 🌐 Runs locally in browser via Flask
* 🖥️ Clean and responsive UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Compression Engine:** Ghostscript (CLI)
* **Frontend:** HTML, CSS
* **Other:** subprocess module for CLI integration

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-compressor.git
cd pdf-compressor
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ghostscript

Download and install Ghostscript from:
👉 https://www.ghostscript.com/download/gsdnld.html

Make sure it is added to your system PATH or update the Ghostscript path in `app.py`.

---

### 5️⃣ Run the application

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
pdf-compressor/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploads/        # ignored (runtime files)
├── compressed/     # ignored (output files)
└── .gitignore
```

---

## ⚠️ Notes

* The `uploads` and `compressed` folders are ignored by Git and created automatically during runtime.
* Ghostscript is required for compression to work.

---

## 🎯 Future Improvements

* Standalone EXE packaging
* Drag & drop upload
* Compression preview statistics
* Automatic file cleanup
* Deployment to cloud server

---

## 👨‍💻 Author

**Avirup Basak**
BCA Student | Aspiring AI Developer

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---
