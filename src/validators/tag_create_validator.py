from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpCreateUnprocessableEntityError

def create_validator(request: any) -> None:
  validator = Validator({
      "product_code" : {
          "type" : "string",
          "required" : True,
          "empty" : True
      }
  })

  response = validator.validate(request)
  if not response:
    raise HttpCreateUnprocessableEntityError(validator.errors)
