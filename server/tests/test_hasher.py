from src.hasher import Hasher
import re


def test_hashing():
    op = Hasher.hash("password")
    hash_reg = r"[$]2[a-z][$][0-9]+[$][a-zA-Z0-9]+"
    assert re.search(hash_reg, op) is not None
    assert not (op == "password")
    assert type(op) == str
