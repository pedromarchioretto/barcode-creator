from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_create_controller import TagCreateController

class TagCreatorView:
  '''
    class to interact with http
  '''
  def validate_and_create(self, http_requests : HttpRequest) -> HttpResponse:
    body = http_requests.body
    product_code = body["product_code"]

    create_controller = TagCreateController()
    formatted_response = create_controller.create(product_code)

    #retorno http
    return HttpResponse(status_code=200, body=formatted_response)
