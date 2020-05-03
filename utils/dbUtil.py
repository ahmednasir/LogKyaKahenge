import pymongo
from config import config

class DBUtil:
    def connectMongo(self):
        try:
            connString = config.config()["DB_STRING"]
            userName = config.config()["DB_PARAMS"]["USER"]
            password = config.config()["DB_PARAMS"]["PASSWORD"]
            db = config.config()["DB_PARAMS"]["DB_NAME"]
            connString = connString.format(username=userName, password= password)
            client = pymongo.MongoClient(connString)
            DB = client[db]
            print("Connected")
            return DB
        except Exception as ex:
            print(ex)
            return False