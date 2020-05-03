from services import infoService
from config import config


class InfoContoller:
    def __init__(self, db):
        self.infoService = infoService.InfoService()
        self.collection = config.config()["COLLECTION_NAME"]["INFO"]
        self.collection = db[self.collection]

    def defaultMethod(self, params):
        try:
            result = []
            if not params:
                result = self.infoService.getAllLogs(collection=self.collection)
                print(result)
            return result
        except Exception as ex:
            print(ex)
            return False


class InfoFilterController:
    def __init__(self, db):
        self.infoService = infoService.InfoService()
        self.collection = config.config()["COLLECTION_NAME"]["INFO"]
        self.collection = db[self.collection]

    def masterMethod(self,filterType, conditions):
        try:
            result = []
            if filterType.lower() == "search":
                result = self.infoService.getSearchedLogs(self.collection, conditions)
                print(result)
            return result
        except Exception as ex:
            print(ex)
            return []

