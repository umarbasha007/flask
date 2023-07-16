from flask import Blueprint, request, jsonify
from controllers.user_controller import user_login_controller

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/login', methods=['POST'])
def process_post_route():
    request_data = request.get_json()
    result = user_login_controller(request_data)

    return jsonify(result), result["stats_code"]
