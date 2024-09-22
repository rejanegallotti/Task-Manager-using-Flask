import unittest
from models import User

class TestUserModelCase(unittest.TestCase):

    def test_user_creation(self):
        user = User(username="test_user", password="test_password")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")
        self.assertIsNone(user.id)  # ID should be assigned after saving

    def test_user_repr(self):
        user = User(username="test_user")
        self.assertEqual(str(user), "User('test_user')")

if __name__ == '__main__':
    unittest.main()