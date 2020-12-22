import re

from src.exceptions import FullNameError, EmailError, UserPasswordError, UserNameError

NAME_LEN = (2, 20)
EMAIL_LEN = (6, 65)
PASSWORD_LEN = (6, 20)
USERNAME_LEN = (6, 20)


def validate_first_last_name(name_str):
    if not (name_str.isalpha() and (1 < len(name_str) < 21)):
        raise FullNameError(name_str)


def validate_email(email_id):
    reg = r"^([a-z0-9]+[._]?)+[@]\w+[.]\w{2,3}$"
    condition_1 = re.search(reg, email_id) is not None
    condition_2 = 5 < len(reg) < 66
    if not (condition_1 and condition_2):
        raise (EmailError(email_id))


def validate_password(password):
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$_!%*#?&])[A-Za-z\d@$_!#%*?&]{6,20}$"
    pat = re.compile(reg)
    if re.search(pat, password) is None:
        raise (UserPasswordError(password))


def validate_username(username):
    reg = r"[a-zA-Z0-9_]{5,20}$"
    pat = re.compile(reg)
    if re.search(pat, username) is None:
        raise (UserNameError(username))
