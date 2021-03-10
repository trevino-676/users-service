import unittest
import json

from app import app, db
from seed_database import insert_data
from app.api.controllers.encrypt_password import encrypt_password, check_password

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        insert_data()
    
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
