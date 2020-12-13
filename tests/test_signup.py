import bcrypt
import pytest

from authentication import signup
from exceptions import UserNameError, EmailError
from setup import setup_db_env_vars

setup_db_env_vars()

# Ideal Input for signup
ip = {
  "first_name" : "Max", 
  "last_name" : "Payne", 
  "email_id" : "max.payne_21@rockstar.com", 
  "username" : "maxpayne_007",
  "password" : "Max@123"
}

def test_signup_first_name_fail():
  fn_ip = ip.copy()
  fn_ip["first_name"] = "Max_21"

  with pytest.raises(UserNameError):
    actual_op = signup(**fn_ip)

def test_signup_first_name_pass():
  try:
    actual_op = signup(**ip)
  except Exception as e:
    pytest.fail(e.message)

def test_signup_last_name_fail():
  fn_ip = ip.copy()
  fn_ip["last_name"] = "Payne_21"

  with pytest.raises(UserNameError):
    actual_op = signup(**fn_ip)

def test_signup_last_name_pass():
  try:
    actual_op = signup(**ip)
  except Exception as e:
    pytest.fail(e.message)

def test_signup_email_fail():
  fn_ip = ip.copy()
  invalid_emails_list = [
    "lolol", 
    "akldjf.laksfj@kldaj", 
    "@kldaj", 
    "@kldaj.asdl",
    "@kldaj.a123674ds", 
    "dsfdsf@kldaj.a123674ds", 
    "@kl8293764.asdl",
    "asfdf@kl8293764.asdl", 
    "asfdf2342@adsfd.asdf",
    "asjkfdhg_kajdsfgh_AKSJGD@alkdjf.kd"
  ]

  with pytest.raises(EmailError):
    for email in invalid_emails_list:
      fn_ip['email_id'] = email
      actual_op = signup(**fn_ip)

def test_signup_email_pass():
  fn_ip = ip.copy()

  try:
    actual_op = signup(**fn_ip)
  except Exception as e:
    pytest.fail(e.message)

# def test_signup_db_check():
#   """
#   Test if data is stored in DB
#   """
#   expected_op = {"first_name" : "Rohan", 
#                 "last_name" : "Awhad", 
#                 "email_id" : "rohanavad007@gmail.com", 
#                 "username" : "rohanawhad",
#                 "password" : "123"
#               }
#   _ = signup(first_name = expected_op['first_name'],
#                      last_name = expected_op['last_name'],
#                      email_id = expected_op['email_id'],
#                      password = expected_op['password'],
#                      username = expected_op['username']
#                     )
#   assert False
