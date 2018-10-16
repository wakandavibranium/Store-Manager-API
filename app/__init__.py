from flask import Flask

# Local import
from instance.config import app_config


def create_app(config_name):
    """Create an instance of Flask and load with environment variables"""

    app = Flask(__name__, instance_relative_config=True)
    
    #Remove trailing slash in url
    app.url_map.strict_slashes = False

    #Import blueprint we created
    from .api.v1 import app_version1

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    #Register blueprint we created
    app.register_blueprint(app_version1)

    return app
