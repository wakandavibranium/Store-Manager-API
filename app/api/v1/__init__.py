from flask import Blueprint
from flask_restplus import Api

#Local import
from .views import namespace_1 as n1

#create a blueprint
app_version1 = Blueprint("v1", __name__, url_prefix="/api/v1")
api_version1 = Api(app_version1)
api_version1.add_namespace(n1,path='/products')