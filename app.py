from flask import Flask, render_template, request
import json
from flask_cors import CORS
from utils import dbUtil
from controllers import InfoController

app = Flask(__name__)
cors = CORS(app)
# Scss(app, static_dir='static/css', asset_dir='assets')



@app.route('/')
def index():
    resp = infoController.defaultMethod(False)
    return render_template("infoLog.html", logs=resp, test="test")

@app.route("/info/<type>")
def getInfoLogsConditional(type):
    try:
        condition = request.args.get("data")
        resp = infoSearchController.masterMethod(type,condition)
        return app.response_class(
                response=json.dumps(resp),
                status=200,
                mimetype='application/json'
            )
    except Exception as ex:
        return app.response_class(
            response=json.dumps([]),
            status=500,
            mimetype='application/json'
        )


if __name__ == '__main__':
    dbUtilClass = dbUtil.DBUtil()
    mongoClient = dbUtilClass.connectMongo()
    if mongoClient:
        infoController = InfoController.InfoContoller(mongoClient)
        infoSearchController = InfoController.InfoFilterController(mongoClient)
        app.run(port=3000)