from flask import Flask, render_template, request, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

app = Flask(__name__)

def generate_key(password):
    kdf = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
    return kdf[:32]

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        data = request.form['data']
        key = generate_key(password)
        encrypted_data = encrypt_data(data, key)
        return render_template('index.html', encrypted_data=encrypted_data.hex())
    return render_template('index.html', encrypted_data=None)

if __name__ == '__main__':
    app.run(debug=True)
