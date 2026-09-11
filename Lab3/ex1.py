import cryptography
print("Cryptography version:", cryptography.__version__)
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"Hello, World!") # b = byte; encoding a byte string
# byte string represents binary data, which is necessary for encryption algorithms to work properly.

print("Encoded Text:", encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print("Decoded Text:", decoded_text) # converts the byte string back to a regular string