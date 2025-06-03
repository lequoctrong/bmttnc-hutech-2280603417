from flask import Flask, request, jsonify

# Import từ các module con (dùng import tuyệt đối)
from cipher.vigenere import VigenereCipher
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Khởi tạo các cipher
vigenere_cipher = VigenereCipher()
caesar_cipher = CaesarCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()

# VIGENERE CIPHER
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# CAESAR CIPHER
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer'}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer'}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# RAILFENCE CIPHER
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer'}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer'}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    if not data or 'key' not in data:
        return jsonify({'error': 'Missing key'}), 400
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# MAIN
if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)