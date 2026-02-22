const uploadInput = document.getElementById("pdfUpload");
const fileNameBox = document.getElementById("fileName");

uploadInput.addEventListener("change", function () {

    if (!this.files.length) {
        fileNameBox.textContent = "";
        return;
    }

    const file = this.files[0];

    /* Convert bytes → readable size */
    function formatSize(bytes){
        const sizes = ["Bytes","KB","MB","GB"];
        if(bytes === 0) return "0 Byte";
        const i = Math.floor(Math.log(bytes)/Math.log(1024));
        return (bytes/Math.pow(1024,i)).toFixed(2)+" "+sizes[i];
    }

    const readableSize = formatSize(file.size);

    fileNameBox.textContent = `${file.name} (${readableSize})`;
});

// Drag and Drop logic
const dropZone = document.querySelector(".upload-box");

/* Prevent browser from opening file */
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.style.borderColor = "#3068cf";
    dropZone.style.background = "#eef3ff";
});

/* Remove highlight when leaving */
dropZone.addEventListener("dragleave", () => {
    dropZone.style.borderColor = "#c7ced6";
    dropZone.style.background = "#fafbfc";
});

/* Handle file drop */
dropZone.addEventListener("drop", (e) => {
    e.preventDefault();

    dropZone.style.borderColor = "#c7ced6";
    dropZone.style.background = "#fafbfc";

    const files = e.dataTransfer.files;

    if(files.length){
        uploadInput.files = files;

        /* Trigger change event manually so filename + size update */
        uploadInput.dispatchEvent(new Event("change"));
    }
});


// Selection box borderColor logic
const selectBox = document.querySelector("select");

selectBox.addEventListener("change", () => {
    selectBox.blur();
});

