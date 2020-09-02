from cryptography.fernet import Fernet
from .secret import AuthSecret


class secretManager:
    def __init__(self):
        self.AuthSecret = AuthSecret()
        self.cipher_suite = Fernet(self.AuthSecret.key)

    def encodeData(self, data):
        encoded_text = self.cipher_suite.encrypt(bytes(data, "utf-8"))
        return encoded_text.decode("utf-8")

    # def decodeData(self, data):
    #     encoded_text = self.cipher_suite.encrypt(bytes(data, 'utf-8'))
    #     decoded_text = self.cipher_suite.decrypt(encoded_text)
    #     return decoded_text.decode("utf-8")
