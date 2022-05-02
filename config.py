import os

PORT = int(os.environ.get('PORT', 4567))
class Config:
    PORT = int(os.environ.get('PORT', 4567))


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True


class Production(Config):
    pass


config = {
    'development': Development,
    'testing': Testing,
    'production': Production,

    'default': Development
}
