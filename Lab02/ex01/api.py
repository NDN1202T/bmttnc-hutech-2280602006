from flask import Flask, request, jsonify
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.caesar import CaesarCipher
from cipher.transposition import TranspositionCipher

# Tạo một instance Flask duy nhất
app = Flask(__name__)

# Khởi tạo các đối tượng cipher
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
vigenere_cipher = VigenereCipher()
caesar_cipher = CaesarCipher()
transposition_cipher = TranspositionCipher()

# Playfair Cipher Routes
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    if not data or 'key' not in data:
        return jsonify({'error': 'Missing key in request'}), 400
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key in request'}), 400
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key in request'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# Rail Fence Cipher Routes
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.json
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except KeyError:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.json
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except KeyError:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Vigenère Cipher Routes
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Caesar Cipher Routes
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Transposition Cipher Routes
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Chạy server một lần duy nhất
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)