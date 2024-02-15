from src.errors.error_render import HttpCreateUnprocessableEntityError
from .tag_create_validator import create_validator

class MockRequest:
  def __init__(self, json) -> None:
    self.json = json

def test_tag_create_validator():
  req = MockRequest(json={ "product_code" : "123" })
  create_validator(req.json)

def test_tag_create_validator_errors():
  req = MockRequest(json={ "product_code" : 123 })

  try:
    create_validator(req.json)
    assert False
  except Exception as exception:
    assert isinstance(exception, HttpCreateUnprocessableEntityError)
