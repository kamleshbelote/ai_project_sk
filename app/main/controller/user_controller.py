from flask import Blueprint, jsonify
from ..services import KBService
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended.typing import ExpiresDelta




bp_user = Blueprint("user", __name__, url_prefix='/api')
user_namespace = Namespace("User", "User Information")


# upload_parser = bp_user.parser()
# upload_parser.add_argument('file', location='files',
#                            type=FileStorage, required=True)

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
        }
    }


@user_namespace.route("/")
@user_namespace.doc(security="jsonWebToken")
class HelloWorld(Resource):    
    @jwt_required()    
    def get(self):
        return jsonify({"message":'This is my first API call!'})

@user_namespace.route("/kb_item")
@user_namespace.doc(security="jsonWebToken")
class KBItem(Resource):
    @jwt_required()
    def get(self):
        service = KBService()
        return jsonify(service.get_new_article().toDict())


@user_namespace.route("/kb_items")
@user_namespace.doc(security="jsonWebToken")
class KBItems(Resource):
    @jwt_required()
    def get(self):
        service = KBService()
        dlist = []
        for item in service.get_articles():
            dlist.append(item.toDict())
        return jsonify(dlist)


@user_namespace.route("/upload_kb")
@user_namespace.doc(security="jsonWebToken")
class UploadKB(Resource):
    @jwt_required()
    def get(self):
        service = KBService()
        dlist = []
        for item in service.get_articles():
            dlist.append(item.toDict())
        return jsonify(dlist)

@user_namespace.route("/get_token")
class AuthJWT(Resource):
    def get(self):
        # expire_delta = 
        token = create_access_token(identity="Kamlesh")
        return jsonify(access_token = token)
    
