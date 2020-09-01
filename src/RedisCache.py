import redis
import json
from .secret import AuthSecret
from .localLogger import localLogger

class ServerlessCache:
    def __init__(self, uniqueId):
        self.AuthSecret = AuthSecret()
        self.rds = redis.Redis(
            host = self.AuthSecret.host,
            port = self.AuthSecret.port, db = self.AuthSecret.db, password = self.AuthSecret.password
        )
        self.uniqueId = uniqueId
        self.localLoggerClient = localLogger()

    def setData(self, cache_key, api):
        api = json.dumps(api)
        self.rds.set(cache_key, api)
        self.rds.expire(cache_key, 618400)
        self.localLoggerClient.loggerOut(self.uniqueId, "Key Updated in Redis")

    def get(self, cache_key):
        # check the key if exist
        cacheData = self.rds.get(cache_key)
        if cacheData:
            cacheData = cacheData.decode("utf-8")
            # cacheData = cacheData.replace("'", "\"")
            cacheData = json.loads(cacheData)
            self.localLoggerClient.loggerOut(self.uniqueId, "Key Found in Redis")
            return cacheData
        else:
            # if key is not exist it will return None
            # so that we can again recheck our db for result
            self.localLoggerClient.loggerOut(self.uniqueId, "Key Not Found in Redis")
            return None
