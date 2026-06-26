/* Displays the selected file name in a span next to the file input, or shows a default placeholder if none is chosen*/
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('digit_image');
    const fileNameSpan = document.getElementById('file-name');

    if (fileInput && fileNameSpan) {
        fileInput.addEventListener('change', function() {
            if (this.files && this.files.length > 0) {
                fileNameSpan.textContent = this.files[0].name;
            } else {
                fileNameSpan.textContent = 'Choose an image or drag it here';
            }
        });
    }
});