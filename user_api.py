from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated user database
users = {
    "chaitanya": {"name": "Chaitanya", "age": 25, "role": "Developer"},
    "ram": {"name": "Ram", "age": 30, "role": "Manager"},
    "sita": {"name": "Sita", "age": 27, "role": "Analyst"}
}

# ──────────────────────────────────────────────
# API 1: GET /hello
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
# API 3: GET /user/<username>
# Example:
#   GET /user/chaitanya
#   GET /user/ram
# ──────────────────────────────────────────────
@app.route("/user/<username>", methods=["GET"])
def get_user(username):

    username = username.lower()  # make case-insensitive

    if username not in users:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    return jsonify({
        "status": "success",
        "message": "User fetched successfully",
        "user": users[username]
    }), 200


# ──────────────────────────────────────────────
# Health Check API (For AKS)
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