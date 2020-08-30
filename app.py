from flask import Flask, request, jsonify, Response
import json
from flask_cors import CORS, cross_origin
from src.processReq import ProcessRequest

app = Flask(__name__,static_url_path='')
CORS(app)

@app.route('/v1',methods=['POST', 'GET'])
def handle():    
    RequestKey = request.get_json(force=True)
    zipcode = RequestKey["zipcode"]

    client = ProcessRequest()
    result ={"data": client.handle(zipcode)}

    result = json.dumps(result)
    resp = Response(result, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(port = int("5000"), debug = True)
