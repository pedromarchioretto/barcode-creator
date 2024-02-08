from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpCreateUnprocessableEntityError

def error_handle(erro: Exception) -> HttpResponse:
  if isinstance(erro, HttpCreateUnprocessableEntityError):
    return HttpResponse(
      status_code = erro.status_code,
      body={
          "errors" : [{
                "title": erro.nome,
                "detail": erro.message
          }]
      }
    )
  return HttpResponse(
      status_code=500,
      body={
        "errors":[{
            "title": "Server Error",
            "detail": str(erro) 
        }]
      }
  )
