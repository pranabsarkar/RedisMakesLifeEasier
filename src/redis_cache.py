import redis
import json
from .secret import AuthSecret
from redis.exceptions import RedisError


class ServerlessCache:
    def __init__(self):
        try:
            self.AuthSecret = AuthSecret()
            self.rds = redis.Redis(
                host=self.AuthSecret.host,
                port=self.AuthSecret.port,
                db=self.AuthSecret.db,
                password=self.AuthSecret.password,
            )
        except RedisError as re:
            print(re)

    def setData(self, cache_key, api):
        try:
            api = json.dumps(api)
            self.rds.set(cache_key, api)
            self.rds.expire(cache_key, 618400)
        except RedisError as re:
            print(re)

    def get(self, cache_key):
        try:
            # check the key if exist
            cacheData = self.rds.get(cache_key)
            if cacheData:
                cacheData = cacheData.decode("utf-8")
                # cacheData = cacheData.replace("'", "\"")
                cacheData = json.loads(cacheData)
                return cacheData
            else:
                # if key is not exist it will return None
                # so that we can again recheck our db for result
                return None
        except RedisError as re:
            print(re)
