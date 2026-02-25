from flask import Flask, jsonify, request

app = Flask(__name__)

# ──────────────────────────────────────────────
# API 1: GET /hello
# Returns a simple greeting message
# ──────────────────────────────────────────────
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "World")  # optional ?name=YourName
    return jsonify({
        "status": "success",
        "message": f"Hello, {name}!",
        "api": "API 1 - Hello"
    })


# ──────────────────────────────────────────────
# API 2: POST /add
# Accepts two numbers and returns their sum
# Body: { "num1": 10, "num2": 20 }
# ──────────────────────────────────────────────
@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    if not data or "num1" not in data or "num2" not in data:
        return jsonify({
            "status": "error",
            "message": "Please provide 'num1' and 'num2' in the request body"
        }), 400

    num1 = data["num1"]
    num2 = data["num2"]
    result = num1 + num2

    return jsonify({
        "status": "success",
        "num1": num1,
        "num2": num2,
        "sum": result,
        "api": "API 2 - Add Numbers"
    })


# ──────────────────────────────────────────────
# Run the server
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("✅ Server is running at http://127.0.0.1:5000")
    print("📌 API 1 → GET  http://127.0.0.1:5000/hello")
    print("📌 API 2 → POST http://127.0.0.1:5000/add")
    app.run(debug=True, port=5000)
