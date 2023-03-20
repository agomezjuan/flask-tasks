class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    # 'default': DevelopmentConfig
}
