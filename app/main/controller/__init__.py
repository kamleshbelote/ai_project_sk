from flask import Blueprint
from flask_restx import Api 
from .user_controller import user_namespace, bp_user
from .admin_controller import admin_namespace, bp_admin
from .search_controller import chat_namespace, bp_chat

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
        }
    }

api_extension_user = Api(bp_user,
                        title='User Information',
                        version='1.0',
                        description='Api for Knowledge Base',
                        doc='/docs',
                        authorizations=authorizations,
                        contact="Kamlesh Belote",
                        contact_email="kamlesh.belote@atriawealth.com"
                    )

api_extension_admin = Api(bp_admin,
                        title='Admin Information',
                        version='1.0',
                        description='Api for Knowledge Base',
                        doc='/docs',
                        authorizations=authorizations,
                    )

api_extension_chat = Api(bp_chat,
                        title='Chat Information',
                        version='1.0',
                        description='Api for Knowledge Base',
                        doc='/docs',
                        authorizations=authorizations,
                    )


api_extension_user.add_namespace(user_namespace)

api_extension_user.add_namespace(admin_namespace)

api_extension_user.add_namespace(chat_namespace)


