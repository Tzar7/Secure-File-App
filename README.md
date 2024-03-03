# Secure-File-App
The Secure File App is a web application designed to demonstrate secure file encryption and decryption using the Advanced Encryption Standard (AES) algorithm. Developed using Python with the Flask web framework, the application provides a user-friendly interface for users to encrypt sensitive data with a password securely.


Workflow:
1:User Input:
Users access the web application through a browser.
They input a password and the data they want to encrypt in the provided form.

2:Server-Side Processing (Flask Application):
Flask handles the incoming HTTP request and extracts the user-provided password and data from the form.
The Flask application generates a cryptographic key using the PBKDF2 function.
The data is encrypted using the AES algorithm in CBC mode with the derived key.

3:Encryption and Decryption:
The AES encryption algorithm is applied to the user-entered data, ensuring secure encryption.
The derived cryptographic key is used for both encryption and decryption processes.

4:Display Encrypted Result:
The Flask application renders the HTML template, including the encrypted result, back to the user.

5:User Interaction:
Users receive real-time feedback with the encrypted data displayed on the web page.
They can copy the encrypted result or take further actions as needed.


1:
generate_key(password) Function:
This function takes a password as input.
It uses the PBKDF2-HMAC-SHA256 key derivation function to derive a cryptographic key from the password.
The key derivation process involves salting the password and performing 100,000 iterations.
The derived key is truncated to 32 bytes (256 bits) to match the key size expected by the AES algorithm.

2:
encrypt_data(data, key) Function:
This function takes data (text to be encrypted) and a cryptographic key as input.
It creates a new AES cipher in Cipher Block Chaining (CBC) mode.
The data is encoded to bytes using UTF-8, padded to the block size using PKCS#7 padding, and then encrypted.
The initialization vector (IV) used during encryption is prepended to the encrypted data.
The resulting ciphertext (IV + encrypted data) is returned.

3:
decrypt_data(encrypted_data, key) Function:
This function takes encrypted_data (ciphertext) and a cryptographic key as input.
It extracts the IV (first 16 bytes) and the actual ciphertext from the input.
A new AES cipher is created with the provided key and IV in CBC mode.
The ciphertext is decrypted, and PKCS#7 padding is removed.
The resulting decrypted data is decoded from bytes to UTF-8 and returned as a string.

4:
Flask Route (@app.route('/')) and index() Function:
This defines the root route ('/') for the Flask application.
The route can handle both GET and POST requests.
For GET requests, it renders the initial HTML template with encrypted_data set to None.
For POST requests (form submission), it processes the form data.
It extracts the password and data from the submitted form.
It generates a cryptographic key using the generate_key() function.
It encrypts the data using the encrypt_data() function.
The resulting encrypted data is converted to hexadecimal format and passed to the HTML template.
The HTML template is rendered, displaying the form and, if applicable, the encrypted data.
