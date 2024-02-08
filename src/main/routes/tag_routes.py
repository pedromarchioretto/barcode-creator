from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_create_view import TagCreatorView
from src.errors.error_render import error_handle
from src.validators.tag_create_validator import create_validator

tag_route_BP = Blueprint('tag_routes', __name__)
@tag_route_BP.route('/create_tag', methods=["POST"])
def create_tag():
  response = None
  try:
    create_validator(request.json)
    tag_create_view = TagCreatorView()
    http_request = HttpRequest(body=request.json)
    response = tag_create_view.validate_and_create(http_requests=http_request)
  except Exception as exception:
    response = error_handle(exception)

  return jsonify(response.body), response.status_code
