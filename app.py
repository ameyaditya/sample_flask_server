from flask import Flask, jsonify, request
from waitress import serve

app = Flask(__name__)

@app.route("/api")
def home():
    return "Hello World"

@app.route("/api/json")
def json():
    return jsonify({"sampleKey": "SampleValue"})

@app.route("/api/dynamic/<did>")
def dynamic(did):
    return jsonify({"key": f"value: {did}"})

@app.route("/api/post_url", methods=['POST'])
def post_url():
    data = request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
    # serve(app, host='0.0.0.0', port=80)