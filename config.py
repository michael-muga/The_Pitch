import os


class Config:
    '''
    General configuration parent class
    '''
    SECRETE_KEY = 'no474tghff8735757t5hf75t77t8'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kimachas@localhost/pitch'
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}