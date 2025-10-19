import os
from flask import Flask
from app.services import services
from .settings import get_env_config
from dotenv import load_dotenv

load_dotenv()


# Inicializar los servicios
def init_services(app):
    for service in services:
        service.init_app(app)


def create_app(config_class=None):
    app = Flask(__name__)

    # Cargar configuracion de entorno
    env_name = os.getenv('FLASK_ENV', 'default')
    config_class = get_env_config(env_name)
    app.config.from_object(config_class)

    # Inicializar servicios
    init_services(app)

    # Registrar blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.health_routes import health_bp
    # from app.routes.habito_routes import habito_bp
    # from app.routes.registro_routes import registro_bp
    # from app.routes.reporte_routes import reporte_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(health_bp, url_prefix='/healthcheck')
    # app.register_blueprint(habito_bp, url_prefix='/habitos')
    # app.register_blueprint(registro_bp, url_prefix='/registros')
    # app.register_blueprint(reporte_bp, url_prefix='/reportes')

    return app