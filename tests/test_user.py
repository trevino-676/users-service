import unittest
import json

from app import app

class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        payload = json.dumps({
            "username": "admin",
            "password": "123123"
        })
        self.token = self.app.post("/auth", 
            headers={"Content-Type": "application/json"},
            data=payload).json["access_token"]
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"JWT {self.token}"
        }
    
    def test_create_user(self):
        payload = json.dumps({
            "username": "testuser",
            "password": "test_pass",
            "email": "testuser@test.com",
            "first_name": "user",
            "last_name": "test",
            "company": "2"
        })

        response = self.app.post("/v1/user/",
            headers=self.header,
            data=payload)

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json["status"])

    def test_get_users(self):
        response = self.app.get("/v1/user/", headers=self.header)

        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(response.json["data"]))
        self.assertEqual("ok", response.json["message"])

    def test_update_user(self):
        payload = json.dumps({
            "id": 12,
            "username": "testuser",
            "password": "test_pass",
            "email": "testuser@test.com",
            "first_name": "user test",
            "last_name": "test",
            "company": "2"
        })

        response = self.app.post(
            "/v1/user/update",
            headers=self.header,
            data=payload
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual("True", response.json["message"])
        self.assertEqual("ok", response.json["status"])