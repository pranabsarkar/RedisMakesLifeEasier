from .redis_cache import ServerlessCache
from .global_db import RelationalDB
from .process_data import ProcessData
from .secret_manager import SecretManager
from .local_logger import LocalLogger
import time
import uuid


class ProcessRequest:
    def __init__(self):
        self.uniqueId = uuid.uuid1().hex
        self.ServerlessCache = ServerlessCache()
        self.RelationalDB = RelationalDB()
        self.processData = ProcessData()
        self.secretManager = SecretManager()
        self.log = LocalLogger()

    def keyConcat(self, zipcode, productName):
        return zipcode + "|" + productName

    def getKey(self, zipcode, productName):
        return self.secretManager.encodeData(self.keyConcat(zipcode, productName))

    def handle(self, zipcode, productName):
        result = None
        try:
            red = self.ServerlessCache
            result = red.get(self.keyConcat(zipcode, productName))

            if result is not None:
                self.log.loggerOut(self.uniqueId, "Found in Redis")
                return result
            else:
                time.sleep(3)
                client = self.RelationalDB
                result = client.getData(int(zipcode), productName)
                # Update the Key in Redis DB
                self.ServerlessCache.setData(
                    self.keyConcat(zipcode, productName),
                    self.processData.handle(result),
                )
                self.log.loggerOut(self.uniqueId, "Found in DB")
                return self.processData.handle(result)
        except Exception as e:
            print(e)
