from flask import Blueprint, request, jsonify
from controllers.post_controller import process_post_controller

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/api/post', methods=['POST'])
def process_post_route():
    request_data = request.get_json()
    result = process_post_controller(request_data)
    return jsonify(result), result["stats_code"]
