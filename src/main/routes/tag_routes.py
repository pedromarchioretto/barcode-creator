from flask import Blueprint, request, jsonify

tag_route_BP = Blueprint('tag_routes', __name__)
@tag_route_BP.route('/create_tag', methods=["POST"])
def create_tag():
  print(request.json)
  return jsonify({"resp": "ok"}), 200
