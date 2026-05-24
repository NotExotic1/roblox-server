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

    # store by userId so multiple players don't overwrite
    uid = str(data.get("userId", "unknown"))

    latest_data[uid] = data

    print("RECEIVED:", data.get("name"))

    return jsonify({"status": "ok"})

@app.route("/api/latest")
def latest():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run()
