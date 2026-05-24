from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"

@app.route("/api/playerdata", methods=["POST"])
def playerdata():
    data = request.json

    print("ROBLOX DATA RECEIVED:")
    print(data)

    return jsonify({"status": "ok"})
