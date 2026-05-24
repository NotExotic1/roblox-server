from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# simple in-memory storage (for testing)
latest_data = {}

@app.route("/")
def home():
    return "Server running"

# IMPORTANT: accepts BOTH GET (testing) and POST (Roblox)
@app.route("/api/playerdata", methods=["GET", "POST"])
def playerdata():
    global latest_data

    if request.method == "GET":
        return jsonify(latest_data)

    data = request.json

    latest_data = {
        "data": data,
        "server_time": time.time()
    }

    print("DATA RECEIVED:", data)

    return jsonify({"status": "ok", "received": True})

@app.route("/api/latest")
def latest():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run()
