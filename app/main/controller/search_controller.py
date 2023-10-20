from flask import Blueprint, jsonify
from ..services import KBService
from flask_restx import Namespace, Resource, fields, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended.typing import ExpiresDelta
from ..services import AIService

bp_chat = Blueprint("chat", __name__, url_prefix='/api')
chat_namespace = Namespace("Chat", "Chat Bot end points")

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
        }
    }

parser = reqparse.RequestParser()
parser.add_argument('search_text', type=str, help='Search Text')

@chat_namespace.route("/search_text")
@chat_namespace.doc(security="jsonWebToken")
class SearchText(Resource):
    
    @chat_namespace.doc(parser=parser)
    def post(self):
        print(self)
        args = parser.parse_args()
        post_var1 = args['search_text']
        aiService = AIService()
        result = aiService.get_answer(post_var1)
        return jsonify({
            'result' : f"{result}"
        })
    