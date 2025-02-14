import os
import cv2
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

# Ensure uploads directory exists inside static
UPLOAD_FOLDER = os.path.join("static", "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files or 'message' not in request.form or 'password' not in request.form:
        return jsonify({'success': False, 'error': 'Missing parameters'})

    image_file = request.files['image']
    message = request.form['message']
    password = request.form['password']

    # Save original image
    original_path = os.path.join(UPLOAD_FOLDER, "original.png")
    image_file.save(original_path)

    img = cv2.imread(original_path)
    if img is None:
        return jsonify({'success': False, 'error': 'Invalid image format'})

    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0

    msg_length = len(message)
    img[n, m, z] = msg_length
    n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3

    for i in range(msg_length):
        img[n, m, z] = d[message[i]]
        n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3

    # Save encrypted image
    enc_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")
    cv2.imwrite(enc_path, img)

    return jsonify({'success': True, 'filename': "uploads/encrypted.png", 'message': 'Encryption successful!'})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'image' not in request.files or 'password' not in request.form:
        return jsonify({'success': False, 'error': 'Missing parameters'})

    image_file = request.files['image']
    entered_password = request.form['password']

    # Save uploaded encrypted image
    enc_path = os.path.join(UPLOAD_FOLDER, "uploaded_encrypted.png")
    image_file.save(enc_path)

    img = cv2.imread(enc_path)
    if img is None:
        return jsonify({'success': False, 'error': 'Invalid image format'})

    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0

    msg_length = img[n, m, z]
    n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3

    message = ""
    for _ in range(msg_length):
        message += c[img[n, m, z]]
        n, m, z = (n + 1) % img.shape[0], (m + 1) % img.shape[1], (z + 1) % 3

    return jsonify({'success': True, 'message': "Secret Message: " + message})

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join("static", "uploads", filename), as_attachment=True)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

