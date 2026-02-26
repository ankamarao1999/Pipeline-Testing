from flask import Flask, jsonify, request
from user_api import user_blueprint   # ⬅ import the blueprint from user_api

app = Flask(__name__)

# Register the user API blueprint
app.register_blueprint(user_blueprint)


# ──────────────────────────────────────────────
# API 1: GET /hello
# Example:
#   GET /hello
#   GET /hello?name=Chaitanya
# ──────────────────────────────────────────────
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")
    return jsonify({
        "status": "success",
        "message": f"Hello, {name}!",
        "api": "API 1 - Hello"
    })


# ──────────────────────────────────────────────
# API 2: POST /add
# Body:
#   {
#     "num1": 10,
#     "num2": 20
#   }
# ──────────────────────────────────────────────
@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    if not data or "num1" not in data or "num2" not in data:
        return jsonify({
            "status": "error",
            "message": "Please provide 'num1' and 'num2' in the request body"
        }), 400

    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        result = num1 + num2
    except Exception:
        return jsonify({
            "status": "error",
            "message": "num1 and num2 must be numbers"
        }), 400

    return jsonify({
        "status": "success",
        "num1": num1,
        "num2": num2,
        "sum": result,
        "api": "API 2 - Add Numbers"
    })


# ──────────────────────────────────────────────
# Health Check API (Very Important for AKS)
# ──────────────────────────────────────────────
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


# ──────────────────────────────────────────────
# Run Application
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("🚀 Flask server running on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)