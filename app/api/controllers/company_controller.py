"""
author: Luis Manuel Torres Trevino
description: This file contains the company controller
"""
from app.models.company import Company
from app import db


class CompanyController:

    def add_company(self, data):
        try:
            company = Company(data["name"], data["description"])
            db.session.add(company)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error al insertar la compania")
            print(e)
            return False
    
    def get_companies(self, filters):
        if "id" in filters:
            companies = Company.query \
                            .filter_by(active = filters["actives"], id = filters["id"]) \
                            .all()
        else:
            companies = Company.query.filter_by(active = filters["actives"]).all()
        
        return [company.to_dict() for company in companies]
    
    def update_company(self, data):
        try:
            company = Company.query.filter_by(id = data["id"]).first()
            company.name = data["name"] if "name" in data else company.name
            company.description = data["description"] if "description" in data \
                else company.description
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_company(self, id):
        try:
            company = Company.query.filter_by(id = id).first()
            company.active = False
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
