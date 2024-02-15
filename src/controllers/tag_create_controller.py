from typing import Dict
from src.drivers.bar_code_handler import BarCodeHandler

class TagCreateController:
  '''
    Responsible to implementing business rules
  '''
  def create(self, product_code: str) -> Dict:
    path_from_tag = self.__create_barcode(product_code)
    formatted_response = self.__formatted_response(path_from_tag)
    return formatted_response

  def __create_barcode(self, product_code: str) -> str:
    barcode_handler = BarCodeHandler()
    path_from_tag = barcode_handler.create_barcode(product_code)
    return path_from_tag

  def __formatted_response(self, path_from_tag: str) -> Dict:
    return{
      "data":{
          'type': 'Tag Image',
          'count': 1,
          'path': f"{path_from_tag}.png"
      }
    }
