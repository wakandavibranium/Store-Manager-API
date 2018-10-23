import unittest
import json

# Local import
from ... import create_app
from ...api.v1.models import UserModel


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        """Initialize Flask app and declare variables to
        be used before running every test"""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.content_type = "application/json"
        self.users = {
            "name": "John Doe",
            "email": "johndoe@gmail.com",
            "phone": "0722123456",
            "role": "John Doe",
            "password": "12345"}

        self.user_login = {
            "email": "johndoe@gmail.com",
            "password": "12345"}

    def tearDown(self):
        """Empty the dictionaries and list after running every test"""

        self.users = {}
        self.user_login = {}
        UserModel.registered_users = []

    def test_admin_can_get_all_registered_users(self):
        """Test admin can get all registered users"""

        response = self.client.post(
            "/api/v1/auth/signup",
            data=json.dumps(
                self.users),
            content_type=self.content_type)

        response = self.client.get(
            "/api/v1/auth/signup",
            content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_admin_can_signup_a_user(self):
        """Test admin can add a user"""

        response = self.client.post(
            "/api/v1/auth/signup",
            data=json.dumps(
                self.users),
            content_type=self.content_type)
        self.assertEqual(response.status_code, 201)

    def test_user_can_login(self):
        """Test user can login"""

        response = self.client.post(
            "/api/v1/auth/signup",
            data=json.dumps(
                self.users),
            content_type=self.content_type)

        response = self.client.post(
            "/api/v1/auth/login",
            data=json.dumps(
                self.user_login),
            content_type=self.content_type)
        self.assertEqual(response.status_code, 201)
