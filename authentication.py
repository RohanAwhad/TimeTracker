import bcrypt
import re

from exceptions import UserNameError, EmailError

def validate_first_last_name(name_str):
  if not name_str.isalpha(): raise UserNameError(name_str)

def validate_email(email_id):
  email_regex = r'^([a-z0-9]+[._]?)+[@]\w+[.]\w{2,3}$'
  if re.search(email_regex, email_id) is None:
    raise(EmailError(email_id))


def signup(first_name, last_name, email_id, password, username):
  validate_first_last_name(first_name)
  validate_first_last_name(last_name)
  validate_email(email_id)

  

# salt = bcrypt.gensalt()
# hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
  
