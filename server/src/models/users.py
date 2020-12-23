class User:
    def __init__(first_name, last_name, email_id, password, username):
        self.set_user(first_name, last_name, email_id, password, username)

    def set_user(self, first_name, last_name, email_id, password, username):
        self._first_name = first_name
        self._last_name = last_name
        self._email_id = email_id
        self._password = password
        self._username = username

    @property
    def first_name(self):
        return self._first_name