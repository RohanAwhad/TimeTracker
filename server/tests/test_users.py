from src.models.user import User

user_data = {
    "first_name": "Max",
    "last_name": "Payne",
    "email_id": "max.payne_21@rockstar.com",
    "username": "maxpayne_021",
    "password": "Max@123",
}
max_payne = None


def test_create_user():
    max_payne = User(**user_data)


# def test_get_first_name():
#     assert max_payne