import bcrypt


class Hasher:
    @staticmethod
    def hash(self, string_to_hash):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(string_to_hash.encode("utf-8"), salt)
        return hashed_password.decode()
