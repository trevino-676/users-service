import unittest
import json

from app import app, db
from app.api.controllers.user_controller import UserController
from app.api.controllers.company_controller import CompanyController
from app.api.controllers.encrypt_password import encrypt_password, check_password

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

        controller = UserController()
        company_controller = CompanyController()
        
        compan = company_controller.add_company({
            "name": "test",
            "description": ""
        })

        user = controller.new_user(
            username="admin",
            mail="test@test.com",
            first_name="user",
            last_name="test",
            password="123123",
            company=1
        )

    
    def test_successful_signup(self):
        payload = json.dumps({
            "username": "admin",
            "password": "123123"
        })

        response = self.app.post("/auth", 
            headers={"Content-Type": "application/json"},
            data=payload)
        
        self.assertEqual(str, type(response.json["access_token"]))
        self.assertEqual(200, response.status_code)
    
    def test_bad_password(self):
        payload = json.dumps({
            "username": "admin",
            "password": "secret"
        })

        response = self.app.post("/auth",
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual("Invalid credentials", response.json["description"])
        self.assertEqual(401, response.status_code)
    
    def test_not_active_user_signup(self):
        payload = json.dumps({
            "username": "admin2",
            "password": "123123"
        })

        response = self.app.post("/auth",
            headers={"Content-Type": "application/json"},
            data=payload)

        self.assertEqual("Invalid credentials", response.json["description"])
        self.assertEqual(401, response.status_code)

    def test_encrypt_password(self):
        password = "test-password"
        hash_pass = encrypt_password(password)
        self.assertEqual(str, type(hash_pass))

    def test_check_password(self):
        password = "test-password"
        hash_pass = encrypt_password(password)
        
        is_correct = check_password(password, hash_pass)
        self.assertEqual(True, is_correct)

        is_correct = check_password("hola", hash_pass)
        self.assertEqual(False, is_correct)
