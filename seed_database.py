from alembic import op

from app.models.users import User
from app.models.company import Company


def insert_data():
    company_data = {
        "name": "Test Company",
        "description": ""
    }

    company = Company(company_data["name"], company_data["description"])
    company.save()
    id = Company.query(Company.id).filter(name=company_data["name"]).first()

    user_data = {
        "username": "admin",
        "password": "123123",
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "company": id if id else Company.query(id).filter(name=company_data["name"]).first()
    }

    other_user_data = {
        "username": "admin2",
        "password": "123123",
        "first_name": "test",
        "last_name": "user",
        "email": "test@test.com",
        "company": id if id else Company.query(id).filter(name=company_data["name"]).first()
    }

    user = User(
        user_data["username"],
        user_data["email"],
        user_data["first_name"],
        user_data["last_name"],
        user_data["password"],
        user_data["company"]
    ).save()
    
    other_user_data = User(
        other_user_data["username"],
        other_user_data["email"],
        other_user_data["first_name"],
        other_user_data["last_name"],
        other_user_data["password"],
        other_user_data["company"]
    ).save()
