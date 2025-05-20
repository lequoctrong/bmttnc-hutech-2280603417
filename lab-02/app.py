from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router for Caesar Cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route for encryption
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText'].upper()
        key = int(request.form['inputKeyPlain'])
        caesar = CaesarCipher()
        encrypted_text = caesar.encrypt_text(text, key)
        return render_template('caesar.html', result=f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}")
    except (ValueError, KeyError):
        return render_template('caesar.html', result="Error: Invalid input. Please check your text and key.")

# Route for decryption
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText'].upper()
        key = int(request.form['inputKeyCipher'])
        caesar = CaesarCipher()
        decrypted_text = caesar.decrypt_text(text, key)
        return render_template('caesar.html', result=f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}")
    except (ValueError, KeyError):
        return render_template('caesar.html', result="Error: Invalid input. Please check your text and key.")

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5950, debug=True)