import redis
import json
from .secret import AuthSecret

class ServerlessCache:
    def __init__(self):
        self.AuthSecret = AuthSecret()
        self.rds = redis.Redis(
            host = self.AuthSecret.host,
            port = self.AuthSecret.port, db = self.AuthSecret.db, password = self.AuthSecret.password
        )

    def setData(self, cache_key, api):
        # dumps is to convert json data to string because redis accept string data
        api = json.dumps(api)
        # syntax to store response first param is key and second is value
        self.rds.set(cache_key, api)
        # here is the expire time for cache data you can change the time(in seconds)
        self.rds.expire(cache_key, 618400)

    def get(self, cache_key):
        # check the key if exist
        cacheData = self.rds.get(cache_key)
        if cacheData:
            # as we stored api response in string format
            # we have to convert it into json data
            cacheData = cacheData.decode("utf-8")
            # cacheData = cacheData.replace("'", "\"")
            cacheData = json.loads(cacheData)
            return cacheData
        else:
            # if key is not exist it will return None
            # so that we can again recheck our db for result
            return None
