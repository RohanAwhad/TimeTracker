from src.models.user import User
from warnings import warn

user_data = {
    "first_name": "Max",
    "last_name": "Payne",
    "email_id": "max.payne_21@rockstar.com",
    "username": "maxpayne_021",
    "password": "Max@123",
}


max_payne = User(**user_data)


def test_get_first_name():
    assert max_payne.first_name == user_data["first_name"]


def test_get_last_name():
    assert max_payne.last_name == user_data["last_name"]
