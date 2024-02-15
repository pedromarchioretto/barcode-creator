from unittest.mock import patch
from src.controllers.tag_create_controller import TagCreateController
from src.controllers.tag_create_controller import BarCodeHandler

class MockProduct():
  def __init__(self, product_code) -> None:
    self.product_code = product_code

@patch.object(BarCodeHandler, "create_barcode")
def test_create(mock_barcode_handler):
  mock_value = MockProduct("Image-Path").product_code
  mock_barcode_handler.return_value = mock_value
  tag_create_controller = TagCreateController()
  response = tag_create_controller.create(mock_value)

  assert isinstance(response, dict)
  assert "data" in response
  assert "type" in response["data"]
  assert "count" in response["data"]
  assert "path" in response["data"]

  assert isinstance(response["data"], dict)
  assert isinstance(response["data"]["type"], str)
  assert isinstance(response["data"]["count"], int)

  assert response["data"]["type"] == "Tag Image"
  assert response["data"]["count"] == 1
  assert response["data"]["path"] == f"{mock_value}.png"
