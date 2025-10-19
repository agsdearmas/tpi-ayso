from app.services.base_service import BaseService
from .db_connector import MongoConnector


class MongoService(BaseService):

    def __init__(self):
        self.connector = None

    def init_app(self, app):
        # Inicializar el conector y adjuntar la instancia actual
        self.connector = MongoConnector()
        app.mongo_service = self

        # Marcar el servicio como inicializada
        app.config['MONGO_SERVICE_INIT'] = True
        return self

    def get_db(self, alias='default', db_name=None):
        return self.connector.get_db(alias, db_name)
