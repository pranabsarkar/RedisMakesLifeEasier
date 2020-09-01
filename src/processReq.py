from .RedisCache import ServerlessCache
from .GlobalDb import RelationalDB
from .processData import processData
from .secretManager import secretManager
import time


class ProcessRequest:
    def __init__(self, uniqueId):
        self.uniqueId = uniqueId
        self.ServerlessCache = ServerlessCache(uniqueId)
        self.RelationalDB = RelationalDB(uniqueId)
        self.processData = processData()
        self.secretManager = secretManager()

    def keyConcat(self, zipcode, productName):
        return zipcode + "|" + productName

    def createKey(self, zipcode, productName):
        return self.secretManager.encodeData(
            self.keyConcat(zipcode, productName)
        )

    def getKey(self, zipcode, productName):
        return self.secretManager.decodeData(
            self.keyConcat(zipcode, productName)
        )

    def handle(self, zipcode, productName):
        result = None

        red = self.ServerlessCache
        result = red.get(self.getKey(zipcode, productName))

        if result is not None:
            return result
        else:
            time.sleep(3)
            client = self.RelationalDB
            result = client.getData(int(zipcode), productName)
            # Update the Key in Redis DB
            self.ServerlessCache.setData(
                self.createKey(zipcode, productName),
                self.processData.handle(result)
            )
            return self.processData.handle(result)
