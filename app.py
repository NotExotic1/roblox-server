from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {}

@app.route("/")
def home():
    return "Server running"

@app.route("/api/playerdata", methods=["POST"])
def playerdata():
    global latest_data

    data = request.get_json()
    latest_data = data

    print("🔥 RECEIVED DATA:", data["name"])

    return jsonify({"status": "ok"})

@app.route("/api/latest")
def latest():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run()
