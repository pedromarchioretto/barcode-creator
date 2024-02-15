from unittest.mock import patch
from src.controllers.tag_create_controller import TagCreateController
from .tag_create_view import TagCreatorView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


@patch.object(TagCreateController, "create")
def test_validate_and_create(mock_create_controller):
  body = {
    "product_code" : "teste123"
  }
  mock_create_controller.return_value = body
  http_request = HttpRequest(body=body)
  tag_create_view = TagCreatorView()
  response = tag_create_view.validate_and_create(http_requests=http_request)

  assert isinstance(response, HttpResponse)  #verifica se a response é do tipo HttpResponse
