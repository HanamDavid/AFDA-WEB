document.getElementById("upload-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    let fileInput = document.getElementById("audio-file");
    if (!fileInput.files.length) {
        alert("Select an audio-file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    let resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<p class='text-warning'>processing...</p>";

    try {
        let response = await fetch("http://localhost:8000/predict/", {
            method: "POST",
            body: formData
        });

        let data = await response.json();

        if (response.ok) {
            resultDiv.innerHTML = `<p class='text-success'>It looks like you... <strong>${data.prediction}</strong> alzheimer</p>`;
        } else {
            resultDiv.innerHTML = `<p class='text-danger'>Error: ${data.detail}</p>`;
        }
    } catch (error) {
        resultDiv.innerHTML = "<p class='text-danger'>Could not connect to the server.</p>";
    }
});

