from cryptography.fernet import Fernet
from .secret import AuthSecret

class secretManager:
    def __init__(self):
        self.AuthSecret = AuthSecret()
        self.cipher_suite = Fernet(AuthSecret.key)
    
    def encodeData(self, data):
        encoded_text = self.cipher_suite.encrypt(b"{}".format(data))
        return encoded_text

    def decodeData(self, data):
        decoded_text = self.cipher_suite.decrypt(data)
        return decoded_text.decode("utf-8")
