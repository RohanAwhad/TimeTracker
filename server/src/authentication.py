import bcrypt

from src.validations import (
    validate_first_last_name,
    validate_email,
    validate_password,
    validate_username,
)


def signup(first_name, last_name, email_id, password, username):
    validate_first_last_name(first_name)
    validate_first_last_name(last_name)
    validate_email(email_id)
    validate_password(password)
    validate_username(username)
