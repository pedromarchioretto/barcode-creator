from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
  '''
    class to interact with http
  '''
  def validate_and_create(self, http_requests : HttpRequest) -> HttpResponse:
    body = http_requests.body
    product_code = body["product_code"]

    print (product_code)
    #logica de regra de negocios

    #retorno http
    return HttpResponse(status_code=200, body={"hello": "world"})
