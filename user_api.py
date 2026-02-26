from flask import Blueprint, jsonify

user_blueprint = Blueprint("user_api", __name__)

# Dummy user data
users = {
    1: {"id": 1, "name": "Chaitanya", "role": "Admin"},
    2: {"id": 2, "name": "Ravi", "role": "Developer"},
    3: {"id": 3, "name": "Kiran", "role": "Tester"},
}

# ──────────────────────────────
# API: GET /user/<id>
# ──────────────────────────────
@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({
            "status": "success",
            "message": "User fetched successfully",
            "user": users[user_id]
        })
    else:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
        