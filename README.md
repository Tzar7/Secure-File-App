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

Process Diagram:
+------------------------+       +----------------------+       +------------------------+
|                        |       |                      |       |                        |
|      User's Browser    |       |   Flask Application  |       |   AES Encryption/      |
|                        |       |                      |       |    Decryption Module   |
+------------------------+       +----------+-----------+       +----------+-------------+
                                            |                            |
                                            |                            |
                                    +-------v---------------------+  |
                                    |                           |  |
                                    |  Handle HTTP Request     |  |
                                    |                           |  |
                                    +-----------+---------------+  |
                                                |                  |
                                                v                  |
                                          +-----+-------------+    |
                                          |                   |    |
                                          |  Process Form Data|    |
                                          |                   |    |
                                          +-------------------+    |
                                                |                  |
                                                v                  |
                                          +-----+-------------+    |
                                          |                   |    |
                                          | Generate Key      |    |
                                          |                   |    |
                                          +-------------------+    |
                                                |                  |
                                                v                  |
                                          +-----+-------------+    |
                                          |                   |    |
                                          |  Encrypt Data     |    |
                                          |                   |    |
                                          +-------------------+    |
                                                |                  |
                                                v                  |
                                          +-----+-------------+    |
                                          |                   |    |
                                          |  Render HTML      |    |
                                          |                   |    |
                                          +-------------------+    |
                                                |                  |
                                                v                  |
                                          +-----+-------------+    |
                                          |                   |    |
                                          |   Display Result  |    |
                                          |                   |    |
                                          +-------------------+    |
