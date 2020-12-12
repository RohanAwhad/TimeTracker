import bcrypt

def signup(first_name, last_name, email_id, password, username):
  
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
  
  return {
      "first_name" : first_name,
      "last_name" : last_name,
      "email_id" : email_id,
      "hashed_password" : hashed_password,
      "username" : username
  }
  
