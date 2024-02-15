from .error_types.http_unprocessable_entity import HttpCreateUnprocessableEntityError
from ..views.http_types.http_response import HttpResponse
from .error_render import error_handle

def test_error_handler():
  message = "error_message"
  unproc_error = HttpCreateUnprocessableEntityError(message)

  assert isinstance(unproc_error, HttpCreateUnprocessableEntityError)

  response = error_handle(unproc_error)

  assert isinstance(response, HttpResponse)
  assert response.status_code
  assert isinstance(response.status_code, int)
  assert response.status_code == 422
  assert response.body
  assert "errors" in response.body
  assert len(response.body["errors"]) == 1
  assert len(response.body["errors"][0]) == 2
  assert "title" in response.body["errors"][0]
  assert "detail" in response.body["errors"][0]
  assert response.body["errors"][0]["title"] == "Unprocessable Entity"
  assert response.body["errors"][0]["detail"] == message


  class ExceptionTest(Exception):
    pass

  exception_message = "teste de exception"
  try:
    raise ExceptionTest(exception_message)
  except ExceptionTest as exception:
    response = error_handle(exception)

  assert isinstance(response, HttpResponse)
  assert response.status_code
  assert isinstance(response.status_code, int)
  assert response.status_code == 500
  assert response.body
  assert "errors" in response.body
  assert len(response.body["errors"]) == 1
  assert len(response.body["errors"][0]) == 2
  assert "title" in response.body["errors"][0]
  assert "detail" in response.body["errors"][0]
  assert response.body["errors"][0]["title"] == "Server Error"
  assert response.body["errors"][0]["detail"] == exception_message
