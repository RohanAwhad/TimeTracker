import bcrypt
import os
import pytest
import re

from authentication import signup, hashing
from exceptions import UserNameError, EmailError, UserPasswordError, FullNameError
from setup import setup_db_env_vars
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Ideal Input for signup
ip = {
  "first_name" : "Max", 
  "last_name" : "Payne", 
  "email_id" : "max.payne_21@rockstar.com", 
  "username" : "maxpayne_021",
  "password" : "Max@123"
}

def test_first_name_fail():
  fn_ip = ip.copy()
  fn_ip["first_name"] = "Max_21"

  with pytest.raises(FullNameError):
    signup(**fn_ip)

def test_first_name_pass():
  try:
    signup(**ip)
  except Exception as e:
    pytest.fail(e.message)

def test_last_name_fail():
  fn_ip = ip.copy()
  fn_ip["last_name"] = "Payne_21"

  with pytest.raises(FullNameError):
    signup(**fn_ip)

def test_last_name_pass():
  try:
    signup(**ip)
  except Exception as e:
    pytest.fail(e.message)

def test_email_fail():
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
    "asjkfdhg_kajdsfgh_AKSJGD@alkdjf.kd",
    "asjkfdhg_kajdsfgh_asjkfdhg_kajdsfgh_asjkfdhg_kajdsfgh_jkahgesdfjkhad.gsfjkasdgfkjhsdbzf_hja@alkdjf.kd"
  ]

  with pytest.raises(EmailError):
    for email in invalid_emails_list:
      fn_ip['email_id'] = email
      signup(**fn_ip)

def test_email_pass():
  try:
    signup(**ip)
  except Exception as e:
    pytest.fail(e.message)

def test_password_fail():
  fn_ip = ip.copy()

  invalid_passwords_list = [
    "",
    "123", 
    "pass",
    "password",
    "password123",
    "passball_123", # Needs uppercase with it
    "Temp",
    "Password$",
    "MAX@097", # no lowercase letters
    "1234543@",
    "Password_is_Too_Strong_For_theDB@27986500" # Too long
  ]

  with pytest.raises(UserPasswordError):
    for password in invalid_passwords_list:
      fn_ip['password'] = password
      signup(**fn_ip)

def test_password_pass():
  fn_ip = ip.copy()

  valid_passwords_list = [
    "Reklh_8u7",
    "fgfs$5647PKL",
    "674@mhkjKO",
    "#$@kladjfKL76"
  ]

  try:
    signup(**ip)
    for password in valid_passwords_list:
      fn_ip['password'] = password
      signup(**fn_ip)
  except Exception as e:
    pytest.fail(e.message)


def test_username_fail():
  fn_ip = ip.copy()

  invalid_usernames_list = [
    "MaxPayne@", # Only '_' is allowed
    "Max Payne", # No spaces
    "289374",
    "M_2"
  ]

  with pytest.raises(UserNameError):
    for username in invalid_usernames_list:
      fn_ip['username'] = username
      signup(**fn_ip)

def test_username_pass():
  fn_ip = ip.copy()

  valid_usernames_list = [
    "Max_Payne_21",
    "maxpayne",
    "maxpayne097",
    "SL500"
  ]

  try:
    signup(**ip)
    for username in valid_usernames_list:
      fn_ip['username'] = username
      signup(**fn_ip)
  except Exception as e:
    pytest.fail(e.message)

def test_hashing():
  op = hashing(ip['password'])
  hash_reg = r"[$]2[a-z][$][0-9]+[$][a-zA-Z0-9]+"
  assert re.search(hash_reg, op) is not None
  assert not(op == ip['password'])
  assert type(op) == str

def test_user_saving():
  signup(**ip)
  setup_db_env_vars()
  db_user = os.getenv("DB_USER")
  db_password = os.getenv("DB_PASSWORD")
  db_host = os.getenv("DB_HOST")
  db_port = os.getenv("DB_PORT")
  db_name = os.getenv("DB_NAME")

  conn = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
  engine = create_engine(conn)

  Session = sessionmaker(bind=engine)
  session = Session()
  query = session.query(User).filter_by(email_id=ip['email_id'])
  try:
    user = query.one()
    for k, v in ip:
      if k == 'password':
        assert bcrypt.checkpw(v.encode("utf-8"), user.__getattribute__[k])
      else:
        assert v == user.__getattribute__[k]

  except:
    pytest.fail(f"Multiple entries with {email_id} as an email id")
