def config():
    return {
        "DB_PARAMS": {
            "USER": "rhino",
            "PASSWORD": "Ff9Aa4nin31BUaiK",
            "DB_NAME": "Logs",
        },
        "COLLECTION_NAME": {
            "INFO": "infoLogs",
            "ERROR": "errorLogs"
        },
        "DB_STRING":  "mongodb+srv://{username}:{password}@cluster0-xjozw.mongodb.net/test?retryWrites=true&w=majority"
    }