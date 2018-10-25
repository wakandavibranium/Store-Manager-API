from flask import Blueprint
from flask_restplus import Api

# Local import
from .views import namespace_1 as n1
from .views import namespace_2 as n2
from .views import namespace_3 as n3
from .views import namespace_4 as n4

# create a blueprint
app_version1 = Blueprint("v1", __name__, url_prefix="/api/v1")
api_version1 = Api(app_version1)

# Add namespaces
api_version1.add_namespace(n1, path='/products')
api_version1.add_namespace(n2, path='/sales')
api_version1.add_namespace(n3, path='/auth/signup')
api_version1.add_namespace(n4, path='/auth/login')
