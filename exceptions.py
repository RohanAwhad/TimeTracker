class UserNameError(Exception):
  """Exception raised for errors in the name.

  Attributes:
    salary -- input name which caused the error
    message -- explanation of the error
  """

  def __init__(self, name, message="Name should only include alphabets"):
    self.name = name
    self.message = message
    super().__init__(self.message)

class EmailError(Exception):
  """Exception raised for errors in the name.

  Attributes:
    salary -- input name which caused the error
    message -- explanation of the error
  """

  def __init__(self, email, message="Email ID is invalid"):
    self.email = email
    self.message = message
    super().__init__(self.message)