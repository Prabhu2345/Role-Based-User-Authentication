// Handle the form submission for file upload
document.getElementById('uploadForm').onsubmit = async (e) => {
    e.preventDefault();  // Prevent the default form submission

    const fileInput = document.getElementById('fileInput');
    const statusMessage = document.getElementById('statusMessage');

    if (fileInput.files.length === 0) {
        statusMessage.textContent = "Please select a file.";
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Send file to the server
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();

        if (response.ok) {
            statusMessage.textContent = `Upload successful! File ID: ${result.file_id}`;
            fileInput.value = '';  // Clear the file input
        } else {
            statusMessage.textContent = `Upload failed: ${result.message}`;
        }
    } catch (error) {
        console.error("Error uploading file:", error);
        statusMessage.textContent = "An error occurred while uploading the file.";
    }
};

// Handle checking file upload status
async function checkFileStatus() {
    const fileIdInput = document.getElementById('fileIdInput');
    const statusResult = document.getElementById('statusResult');
    const fileId = fileIdInput.value.trim();

    if (!fileId) {
        statusResult.textContent = "Please enter a file ID.";
        return;
    }

    try {
        const response = await fetch(`/status/${fileId}`);
        const result = await response.json();

        if (response.ok) {
            statusResult.textContent = `Status: ${result.status}`;
        } else {
            statusResult.textContent = result.error || "File not found.";
        }
    } catch (error) {
        console.error("Error checking file status:", error);
        statusResult.textContent = "An error occurred while checking the file status.";
    }
}
