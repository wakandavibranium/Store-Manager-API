import os


class Config(object):
    """Common configurations"""
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
