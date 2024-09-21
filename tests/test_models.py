import unittest
from models import User, Task

class TestUserModelCase(unittest.TestCase):

    def test_user_creation(self):
        user = User(username="test_user", password="test_password")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.password, "test_password")
        self.assertIsNone(user.id)  # ID should be assigned after saving

    def test_user_repr(self):
        user = User(username="test_user")
        self.assertEqual(str(user), "User('test_user')")

class TestTaskModelCase(unittest.TestCase):

    def test_task_creation(self):
        user = User(username="test_user", password="test_password")
        task = Task(content="This is a test task", user_id=user.id)
        self.assertEqual(task.content, "This is a test task")
        self.assertIsNone(task.id)  # ID should be assigned after saving

    def test_task_repr(self):
        user = User(username="test_user")
        task = Task(content="Test task", date_posted="2024-09-20 23:27:00", user_id=user.id)
        self.assertEqual(str(task), "Task('Test task', '2024-09-20 23:27:00', 1)")  # Assuming user.id is 1


if __name__ == '__main__':
    unittest.main()