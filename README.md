# 🎨 Image Steganography Web App

This web application allows users to **hide secret messages inside images (encryption)** and **extract hidden messages from encrypted images (decryption)** using **steganography**. Built with **Flask (Python), OpenCV, HTML, CSS, and JavaScript**, it provides a user-friendly interface for secure communication.

## 🚀 Live Demo

🔗 **Try it now:** [Click Here](https://image-steganography-a2y1.onrender.com)

## ✨ Features

✔ **Encrypt Messages** – Upload an image, enter a secret message, and encrypt it securely.\
✔ **Download Encrypted Image** – Save the encoded image with the hidden message.\
✔ **Decrypt Messages** – Upload the encrypted image, enter the passcode, and retrieve the secret message.\
✔ **User-Friendly UI** – Smooth navigation with buttons for encryption & decryption.\
✔ **Secure & Fast** – Uses image pixel manipulation for data hiding.

## 📂 Tech Stack

- **Frontend**: HTML, CSS, JavaScript 🎨
- **Backend**: Flask (Python) 🐍
- **Libraries**: OpenCV, Waitress, Werkzeug
- **Deployment**: Render

## 🛠️ How It Works

### 🔐 **Encryption:**

1️⃣ Upload an image 📷\
2️⃣ Enter a **secret message** 🔑\
3️⃣ Provide a **password** for security 🔒\
4️⃣ Download the encrypted image 🌆

### 🔓 **Decryption:**

1️⃣ Upload the **encrypted image** 📥\
2️⃣ Enter the **correct password** 🛠️\
3️⃣ Reveal the **hidden message** 📝

## 📌 How to Run Locally

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/panvikrishna1529/image-steganography.git  
cd image-steganography  
```

### 2️⃣ Install Dependencies

Ensure you have **Python 3.8+** installed. Then, install the required Python packages:

```sh
pip install -r requirements.txt  
```

### 3️⃣ Run the Flask App

```sh
python app.py  
```

The server will start at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## 📦 Important Libraries & Installation

To run this project, install the following libraries:

```sh
pip install flask opencv-python waitress Werkzeug  
```

Or install everything at once using:

```sh
pip install -r requirements.txt  
```

## 🌎 Deploying to Render

To deploy this app on **Render**, follow these steps:\
1️⃣ Push your latest changes to **GitHub**\
2️⃣ Go to **Render Dashboard** → Click **New Web Service**\
3️⃣ Connect your GitHub repository\
4️⃣ Set the **Start Command**:

```sh
python app.py  
```

5️⃣ Click **Deploy** 🎉


![Alt Text](demo-results/encrypted.png)
