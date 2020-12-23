import bcrypt


class Hasher:
    def __init__(self):
        pass

    def hash(self, string_to_hash):
        import bcrypt

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(string_to_hash.encode("utf-8"), salt)
        return hashed_password.decode()