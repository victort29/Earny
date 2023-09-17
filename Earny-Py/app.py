#was a test 
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

#opening up end points 
@app.route("/", methods=["GET"])
def getME():
    return 'Hello World'

@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   data = jsonify(data)
   return data


if __name__ == "__main__":
    app.run(debug=True)
