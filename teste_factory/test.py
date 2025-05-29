import unittest
from src.factories.user_factory import UserFactory
from user import User

class TestUserFactory(unittest.TestCase):
    def test_create_default_user(self):
        user = UserFactory.create_user("Antonio")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "Antonio")
        self.assertEqual(user.role, "guest")

    def test_create_user_with_custom_role(self):
        user = UserFactory.create_user("Admin", role="admin")
        self.assertEqual(user.role, "admin")

if __name__ == "__main__":
    unittest.main()
