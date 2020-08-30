from .RedisCache import ServerlessCache
from .GlobalDb import RelationalDB
from .processData import processData

class ProcessRequest:
    def __init__(self):
        self.ServerlessCache = ServerlessCache()
        self.RelationalDB = RelationalDB()
        self.processData = processData()

    def handle(self, payload):
        result = None

        red = self.ServerlessCache
        result = red.get(payload)

        if result is not None:
            return result
        else:
            client = self.RelationalDB
            result = client.getData(int(payload))
            # Update the Key in Redis DB
            self.ServerlessCache.setData(payload, self.processData.handle(result))
            return self.processData.handle(result)
