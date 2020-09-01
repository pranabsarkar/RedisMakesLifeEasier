class AuthSecret:
    def __init__(self):
        self.LoadEnv()
    
    def LoadEnv(self):
        self.host = ""
        self.port = ""
        self.db = 0
        self.password = ""
        self.key = b'0hJcTXjeNhU-QQTzbWC4xmpwHFl0Co-xCR1GsAECPqE='
