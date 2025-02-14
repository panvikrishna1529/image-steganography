function showEncryption() {
    document.getElementById("encryption-section").classList.remove("hidden");
    document.getElementById("decryption-section").classList.add("hidden");
    document.getElementById("encrypt-status").innerText = "";
}

function showDecryption() {
    document.getElementById("decryption-section").classList.remove("hidden");
    document.getElementById("encryption-section").classList.add("hidden");
    document.getElementById("decrypt-status").innerText = "";
}

function encryptImage() {
    let imageFile = document.getElementById("encrypt-image").files[0];
    let message = document.getElementById("secret-message").value;
    let password = document.getElementById("encryption-password").value;
    
    if (!imageFile || !message || !password) {
        alert("⚠️ Please fill all fields!");
        return;
    }

    let formData = new FormData();
    formData.append("image", imageFile);
    formData.append("message", message);
    formData.append("password", password);

    fetch("/encrypt", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("encrypt-status").innerText = "✅ Encryption Successful!";
                let downloadLink = document.getElementById("download-encrypted");
                downloadLink.href = "/static/" + data.filename;
                downloadLink.classList.remove("hidden");
            } else {
                document.getElementById("encrypt-status").innerText = "❌ Error: " + data.error;
            }
        })
        .catch(error => console.error("Error:", error));
}

function decryptImage() {
    let imageFile = document.getElementById("decrypt-image").files[0];
    let password = document.getElementById("decryption-password").value;
    
    if (!imageFile || !password) {
        alert("⚠️ Please fill all fields!");
        return;
    }

    let formData = new FormData();
    formData.append("image", imageFile);
    formData.append("password", password);

    fetch("/decrypt", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("decrypt-status").innerText = "🔑 " + data.message;
            } else {
                document.getElementById("decrypt-status").innerText = "❌ Error: " + data.error;
            }
        })
        .catch(error => console.error("Error:", error));
}
