class Config(object):
    # TODO: Add common config here.
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    # TODO: add production config here.
    pass


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "squad_makers",
    }


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        "db": "test_squad_makers",
    }
