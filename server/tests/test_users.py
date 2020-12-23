from src.models.user import User
from warnings import warn
import pytest

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


def test_get_email_id():
    assert max_payne.email_id == user_data["email_id"]


def test_get_username():
    assert max_payne.username == user_data["username"]


def test_first_name_fail():
    fn_ip = user_data.copy()
    fn_ip["first_name"] = "Max_21"

    with pytest.raises(Exception):
        max_payne.set_user(**fn_ip)
