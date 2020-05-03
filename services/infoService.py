
class InfoService:

    def getAllLogs(self, collection):
        try:
            results = list(collection.find({},{"_id":0}))
            for val in results:
                val['timestamp'] = val['timestamp'].isoformat()
            print(len(results))
            return results

        except Exception as ex:
            print(ex)
            return False

    def getSearchedLogs(self, collection, searchTerm):
        try:
            results = list(collection.find({"message":{'$regex':searchTerm}},{"_id":0}))
            for val in results:
                val['timestamp'] = val['timestamp'].isoformat()
            print(len(results))
            return results
        except Exception as ex:
            print(ex)
            return False