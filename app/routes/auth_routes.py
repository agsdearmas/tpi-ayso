from flask import Blueprint, jsonify


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'msg': 'Login endpoint'})


@auth_bp.route("/register", methods=["POST"])
def register():
    return jsonify({"msg": "Register endpoint"})
