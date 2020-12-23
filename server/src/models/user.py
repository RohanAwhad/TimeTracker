import re


class User:
    def __init__(self, first_name, last_name, email_id, password, username):
        self.set_user(first_name, last_name, email_id, password, username)
        self._NAME_LEN = (2, 20)
        self._EMAIL_LEN = (6, 65)
        self._PASSWORD_LEN = (6, 20)
        self._USERNAME_LEN = (6, 20)

    def set_user(self, first_name, last_name, email_id, password, username):
        if self.is_valid_first_last_name(first_name):
            self._first_name = first_name
        if self.is_valid_first_last_name(last_name):
            self._last_name = last_name
        if self.is_valid_email(email_id):
            self._email_id = email_id
        if self.is_valid_username(username):
            self._username = username
        if self.is_valid_password(password):
            self._password = password

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email_id(self):
        return self._email_id

    @property
    def username(self):
        return self._username

    def is_valid_first_last_name(self, name_str):
        if not (name_str.isalpha() and (1 < len(name_str) < 21)):
            raise Exception(f"{name_str} is not a valid name")
        return True

    def is_valid_email(self, email_id):
        reg = r"^([a-z0-9]+[._]?)+[@]\w+[.]\w{2,3}$"
        condition_1 = re.search(reg, email_id) is not None
        condition_2 = 5 < len(reg) < 66
        if not (condition_1 and condition_2):
            raise Exception(f"{email_id} is not a valid email id")
        return True

    def is_valid_username(self, username):
        reg = r"[a-zA-Z0-9_]{5,20}$"
        pat = re.compile(reg)
        if re.search(pat, username) is None:
            raise Exception(f"{username} is not a valid username")
        return True

    def is_valid_password(self, password):
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$_!%*#?&])[A-Za-z\d@$_!#%*?&]{6,20}$"
        pat = re.compile(reg)
        if re.search(pat, password) is None:
            raise Exception(f"{password} is not a valid password")
        return True
