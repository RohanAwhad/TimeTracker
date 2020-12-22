class FullNameError(Exception):
    """Exception raised for errors in name.

    Attributes:
      name -- input name which caused the error
      message -- explanation of the error
    """

    def __init__(self, name, message="Name used is invalid"):
        self.name = name
        self.message = message
        super().__init__(self.message)


class EmailError(Exception):
    """Exception raised for errors in the email.

    Attributes:
      email -- input email which caused the error
      message -- explanation of the error
    """

    def __init__(self, email, message="Email ID is invalid"):
        self.email = email
        self.message = message
        super().__init__(self.message)


class UserPasswordError(Exception):
    """Exception raised for errors in the password.

    Attributes:
      password -- input password which caused the error
      message -- explanation of the error
    """

    def __init__(self, password, message="Password is invalid"):
        self.password = password
        self.message = message
        super().__init__(self.message)


class UserNameError(Exception):
    """Exception raised for errors in the username.

    Attributes:
      username -- input username which caused the error
      message -- explanation of the error
    """

    def __init__(self, username, message="Username is invalid"):
        self.username = username
        self.message = message
        super().__init__(self.message)
