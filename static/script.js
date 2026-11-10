
// ==========================================
// PDF COMPRESSOR + PPTX CONVERTER FILE INPUT
// ==========================================

const uploadInput = document.getElementById("pdfUpload");
const fileNameBox = document.getElementById("fileName");

const pptxUpload = document.getElementById("pptxUpload");
const pptxFileName = document.getElementById("pptxFileName");


// Convert bytes into readable file size
function formatSize(bytes) {
    const sizes = ["Bytes", "KB", "MB", "GB"];

    if (bytes === 0) return "0 Byte";

    const i = Math.floor(Math.log(bytes) / Math.log(1024));

    return (bytes / Math.pow(1024, i)).toFixed(2) + " " + sizes[i];
}


// ==========================================
// PDF COMPRESSOR LOGIC
// ==========================================

if (uploadInput && fileNameBox) {

    uploadInput.addEventListener("change", function () {

        if (!this.files.length) {
            fileNameBox.textContent = "";
            return;
        }

        const file = this.files[0];
        const readableSize = formatSize(file.size);

        fileNameBox.textContent =
            `${file.name} (${readableSize})`;
    });

}


// ==========================================
// PPTX CONVERTER LOGIC
// ==========================================

if (pptxUpload && pptxFileName) {

    pptxUpload.addEventListener("change", function () {

        if (!this.files.length) {
            pptxFileName.textContent = "";
            return;
        }

        const file = this.files[0];
        const readableSize = formatSize(file.size);

        pptxFileName.textContent =
            `${file.name} (${readableSize})`;
    });

}


// ==========================================
// COMPRESSOR DRAG AND DROP LOGIC
// ==========================================

const dropZone = document.querySelector(".upload-box");

if (dropZone && uploadInput) {

    dropZone.addEventListener("dragover", (e) => {
        e.preventDefault();

        dropZone.style.borderColor = "#3068cf";
        dropZone.style.background = "#eef3ff";
    });

    dropZone.addEventListener("dragleave", () => {

        dropZone.style.borderColor = "#c7ced6";
        dropZone.style.background = "#fafbfc";
    });

    dropZone.addEventListener("drop", (e) => {

        e.preventDefault();

        dropZone.style.borderColor = "#c7ced6";
        dropZone.style.background = "#fafbfc";

        const files = e.dataTransfer.files;

        if (files.length) {
            uploadInput.files = files;

            uploadInput.dispatchEvent(
                new Event("change")
            );
        }
    });

}



// ==========================================
// PPTX CONVERTER DRAG AND DROP
// ==========================================

const pptxDropZone = document.querySelector(".converter-dropzone");

if (pptxDropZone && pptxUpload) {

    // Highlight when dragging a file over the area
    pptxDropZone.addEventListener("dragover", (e) => {
        e.preventDefault();

        pptxDropZone.style.borderColor = "#3068cf";
        pptxDropZone.style.background = "#eef3ff";
    });

    // Remove highlight when leaving
    pptxDropZone.addEventListener("dragleave", () => {

        pptxDropZone.style.borderColor = "#c7ced6";
        pptxDropZone.style.background = "#fafbfc";
    });

    // Handle dropped file
    pptxDropZone.addEventListener("drop", (e) => {

        e.preventDefault();

        pptxDropZone.style.borderColor = "#c7ced6";
        pptxDropZone.style.background = "#fafbfc";

        const files = e.dataTransfer.files;

        if (files.length) {

            // Assign dropped file to PPTX input
            pptxUpload.files = files;

            // Trigger filename and size display
            pptxUpload.dispatchEvent(
                new Event("change")
            );
        }
    });
}


// ==========================================
// COMPRESSION MODE SELECT BOX
// ==========================================

const selectBox = document.querySelector("select");

if (selectBox) {
    selectBox.addEventListener("change", () => {
        selectBox.blur();
    });
}
