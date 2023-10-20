from flask import Blueprint, jsonify
from ..services import KBService
from flask_restx import Namespace, Resource, fields, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended.typing import ExpiresDelta
from werkzeug.datastructures import FileStorage

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',type=FileStorage, required=True)

bp_admin = Blueprint("admin", __name__, url_prefix='/api')
admin_namespace = Namespace("Admin", "Admin Information")


@admin_namespace.route("/upload_kb")
@admin_namespace.doc(security="jsonWebToken")
class UploadKB(Resource):
    @jwt_required()
    def get(self):
        return {
            'title' : 'Example'
        }

@admin_namespace.route("/")
@admin_namespace.doc(security="jsonWebToken")
class HelloWorld(Resource):    
    @jwt_required()    
    def get(self):
        return jsonify({"message":'You have access to admin area.'})