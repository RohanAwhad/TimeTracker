import bcrypt
import pytest

from authentication import signup, login

def test_signup_return():
  expected_op = {"first_name" : "Rohan", 
                "last_name" : "Awhad", 
                "email_id" : "rohanavad007@gmail.com", 
                "username" : "rohanawhad",
                "password" : "123"
              }
  actual_op = signup(first_name = expected_op['first_name'],
                     last_name = expected_op['last_name'],
                     email_id = expected_op['email_id'],
                     password = expected_op['password'],
                     username = expected_op['username']
                    )
  for k, v in actual_op.items():
    if k == "hashed_password" : 
      assert bcrypt.checkpw(expected_op["password"].encode("utf-8"), v)
    else:
      assert expected_op[k] == v
      
def test_signup_db_check():
  """
  Test if data is stored in DB
  """
  expected_op = {"first_name" : "Rohan", 
                "last_name" : "Awhad", 
                "email_id" : "rohanavad007@gmail.com", 
                "username" : "rohanawhad",
                "password" : "123"
              }
  _ = signup(first_name = expected_op['first_name'],
                     last_name = expected_op['last_name'],
                     email_id = expected_op['email_id'],
                     password = expected_op['password'],
                     username = expected_op['username']
                    )
  assert False
