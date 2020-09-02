import json
from flask import Flask, request, Response
from flask_cors import CORS
from src.processReq import ProcessRequest


app = Flask(__name__, static_url_path="")
CORS(app)


@app.route("/v1", methods=["POST", "GET"])
def handle():
    RequestKey = request.get_json(force=True)
    zipcode = RequestKey["zipcode"]
    productName = RequestKey["product-name"]

    client = ProcessRequest()
    result = {"data": client.handle(zipcode, productName)}

    result = json.dumps(result)
    resp = Response(result, status=200, mimetype="application/json")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    app.run(port=int("5001"), debug=True)
