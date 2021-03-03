from flask import Blueprint, request, jsonify, make_response
# from werkzeug import check_password_hash, generate_password_hash

from app import app
from app import db
from app import jwt_required
from app.models.company import Company
from app.models.users import User
from app.api.controllers.user_controller import UserController
from app.api.controllers.company_controller import CompanyController

user_controller = UserController()
company_controller = CompanyController()

mod_user = Blueprint('user', __name__, url_prefix='/v1/user')
company_routes = Blueprint('company', __name__, url_prefix='/v1/company')

@mod_user.route('/')
@jwt_required()
def root():
    users = [user.to_dict() for user in user_controller.get_users(0, 0)]
    if len(users) == 0:
        return make_response(jsonify(
            {
                "data": [],
                "message": "No users found"
            }), 401)
    return make_response(jsonify(
        {
            "data": users,
            "message": "ok"
        }
    ), 200)
    


@mod_user.route("/", methods=["POST"])
@jwt_required()
# TODO mandar bad requests
def add_user():
    input_data = request.json
    username = input_data["username"] 
    mail = input_data["email"]
    first_name = input_data["first_name"]
    last_name = input_data["last_name"]
    password = input_data["password"]
    company = input_data["company"]
    is_inserted = user_controller.new_user(username, mail, first_name, last_name, password, company)
    if not is_inserted:
        return make_response(jsonify(
            {"error": "error al insertar el usuarion", "status": "error"}), 401)
    return make_response(jsonify({"status": True, "error": ""}), 200)


@mod_user.route("/update", methods=["POST"])
@jwt_required()
def update_user():
    input_data = request.json
    id = input_data["id"]
    username = input_data["username"]
    mail = input_data["email"]
    first_name = input_data["first_name"]
    last_name = input_data["last_name"]
    password = input_data["password"]
    company = input_data["company"]
    is_updated = user_controller.update_user(id, username, mail, first_name, 
        last_name, password, company)
    
    if not is_updated:
        make_response(
            jsonify({
                "message": "Error al modificar el usuario",
                "status": "error"
            }), 401
        )
    return make_response(jsonify({"message": "True", "status": "ok"}), 200)


@mod_user.route("/delete", methods=["POST"])
@jwt_required()
def delete_user():
    deleted_id = request.json["id"]
    if not user_controller.delete_user(deleted_id):
        return jsonify("{'error': 'Error al eliminar el usuario'}")
    return jsonify("{'is_deleted': True, 'error': '' }")


@company_routes.route("/<id>")
@jwt_required()
def get_companies_by_id(id):
    filters = {"id": id, "actives": True}
    companies = company_controller.get_companies(filters)
    return jsonify(companies)


@company_routes.route("/")
@jwt_required()
def get_companies():
    filters = {"actives": True}
    companies = company_controller.get_companies(filters)
    return jsonify(companies)


@company_routes.route("/", methods=["POST"])
@jwt_required()
def add_company():
    data = request.json
    if not company_controller.add_company(data):
        return make_response(jsonify("{'error': 'Error al insertar la compañia'"), 500)
    return make_response(jsonify("{'is_inserted': True, 'error': ''"), 200)


@company_routes.route("/update", methods=["POST"])
@jwt_required()
def update_company():
    data = request.json
    if not company_controller.update_company(data):
        return make_response(jsonify("{'error': 'Error al actualizar la compañia'"), 500)
    return make_response(jsonify("{'is_updated': True, 'error': ''"), 200)


@company_routes.route("/delete", methods=["POST"])
@jwt_required()
def delete_company():
    deleted_id = request.json["id"]
    if not company_controller.delete_company(deleted_id):
        return make_response(jsonify("{'error': 'Error al eliminar la compañia'"), 500)
    return make_response(jsonify("{'is_updated': True, 'error': ''"), 200)
