const dropArea = document.getElementById("drop-area");
const input = document.getElementById("fileInput");
const browse = document.getElementById("browseBtn");
const preview = document.getElementById("preview");

browse.onclick = () => input.click();

input.onchange = () => {

    showPreview(input.files[0]);

};

dropArea.addEventListener("dragover",(e)=>{

    e.preventDefault();
    dropArea.classList.add("active");

});

dropArea.addEventListener("dragleave",()=>{

    dropArea.classList.remove("active");

});

dropArea.addEventListener("drop",(e)=>{

    e.preventDefault();

    input.files = e.dataTransfer.files;

    showPreview(input.files[0]);

    dropArea.classList.remove("active");

});

function showPreview(file){

    const reader = new FileReader();

    reader.onload = function(e){

        preview.src = e.target.result;
        preview.style.display = "block";

    }

    reader.readAsDataURL(file);

}