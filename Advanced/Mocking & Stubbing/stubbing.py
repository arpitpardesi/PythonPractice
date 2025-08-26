from unittest.mock import patch

def get_user_from_db(id):
    pass

with patch("__main__.get_user_from_db", return_value={'id': 1, 'name': 'Alice'}):
    user = get_user_from_db(1)
    print(user)  # Output: {'id': 1, 'name': 'Alice'}

