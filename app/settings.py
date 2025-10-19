import os
from app.services.mongo_manager.db_config import MongoConfig as dbConfig


class Config:
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'defsupersecret')
    DB_HOST = os.getenv('DB_DEFAULT_HOST', 'mongo')
    DB_PORT = os.getenv('DB_DEFAULT_PORT', '27017')
    DB_USER = os.getenv('DB_DEFAULT_USER', 'mongo_admin')
    DB_PASSWORD = os.getenv('DB_DEFAULT_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_DEFAULT_NAME', 'mongo_db')

    # Lista de configuracion modular
    MONGO_DBS_ALIAS = dbConfig.MONGO_DBS_ALIAS


class DefaultConfig(Config):
    DEBUG = True


class DevelopConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class AnalyticsConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True


# Mapeo de entornos a clases de configuracion
ENV_CONFIGS = {
    'default': DefaultConfig,
    'develop': DevelopConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'analytics': AnalyticsConfig,
    'testing': TestingConfig,
}

# Funcion para obtener la configuracion correcta
def get_env_config(env_name=None):
    """
    Selecciona la clase de configuracion basada en la variable de entorno 'FLASK_ENV' o 'ENV_DEFAULT'.
    """
    # Obtiener el entorno de la variable FLASK_ENV, luego ENV_DEFAULT, y por defecto 'default'.
    env = env_name or os.getenv('FLASK_ENV') or os.getenv('ENV_DEFAULT') or 'default'
    
    return ENV_CONFIGS.get(env, DefaultConfig)
