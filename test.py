import unittest

# from app.main import models as User
from app.main.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'wordpass')

    def test_password_setter(self):
        self.assertTrue(self.new_user.user_password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password(self)

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('wordpass'))






