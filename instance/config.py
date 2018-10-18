import os

class Config(object):
    """Common configurations"""
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/test_db'
    DEBUG = True   


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,    
}