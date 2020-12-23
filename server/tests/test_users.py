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


def test_last_name_fail():
    fn_ip = user_data.copy()
    fn_ip["last_name"] = "Payne_21"

    with pytest.raises(Exception):
        max_payne.set_user(**fn_ip)


def test_email_fail():
    fn_ip = user_data.copy()
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
        "asjkfdhg_kajdsfgh_asjkfdhg_kajdsfgh_asjkfdhg_kajdsfgh_jkahgesdfjkhad.gsfjkasdgfkjhsdbzf_hja@alkdjf.kd",
    ]

    with pytest.raises(Exception):
        for email in invalid_emails_list:
            fn_ip["email_id"] = email
            max_payne.set_user(**fn_ip)


def test_username_fail():
    fn_ip = user_data.copy()

    invalid_usernames_list = [
        "MaxPayne@",  # Only '_' is allowed
        "Max Payne",  # No spaces
        "289374",
        "M_2",
    ]

    with pytest.raises(Exception):
        for username in invalid_usernames_list:
            fn_ip["username"] = username
            max_payne.set_user(**fn_ip)


def test_password_fail():
    fn_ip = user_data.copy()

    invalid_passwords_list = [
        "",
        "123",
        "pass",
        "password",
        "password123",
        "passball_123",  # Needs uppercase with it
        "Temp",
        "Password$",
        "MAX@097",  # no lowercase letters
        "1234543@",
        "Password_is_Too_Strong_For_theDB@27986500",  # Too long
    ]

    with pytest.raises(Exception):
        for password in invalid_passwords_list:
            fn_ip["password"] = password
            max_payne.set_user(**fn_ip)
