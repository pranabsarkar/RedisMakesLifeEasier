class AuthSecret:
    def __init__(self):
        self.LoadEnv()
    
    def LoadEnv(self):
        self.host = ""
        self.port = ""
        self.db = 0
        self.password = ""
