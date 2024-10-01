import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///gerenciador.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Outras configurações gerais

class DevelopmentConfig(Config):
    DEBUG = True
    # Configurações específicas para desenvolvimento

class ProductionConfig(Config):
    DEBUG = False
    # Configurações específicas para produção

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
