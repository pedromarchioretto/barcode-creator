class HttpCreateUnprocessableEntityError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.nome = "Unprocessable Entity"
    self.status_code = 422
