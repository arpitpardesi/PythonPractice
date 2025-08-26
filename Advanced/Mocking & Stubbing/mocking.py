from unittest.mock import Mock

db = Mock()
db.get_user.return_value = {'id': 1, 'name': 'Alice'}


user = db.get_user(1)
print(user)

db.get_user.assert_called_with(1)