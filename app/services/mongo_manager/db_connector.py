import pymongo
from threading import Lock
from flask import current_app


class MongoConnector(object):
    """
    Administra multiples clientes MongoDB (multiDB) con Singleton.
    """
    _instance = None
    _mutex = Lock()


    def __new__(cls, *args, **kwargs):
        with cls._mutex:
            if not cls._instance:
                cls._instance = super(MongoConnector, cls).__new__(cls)
                cls._instance.clients = {}
        return cls._instance


    def _build_uri(self, alias):
        """
        Construye la URI de conexion usando las variables de app.config.
        """
        config = current_app.config
        
        # Obtener componentes
        db_host = config['DB_HOST']
        db_port = config['DB_PORT']
        db_user = config['DB_USER']
        db_pass = config['DB_PASSWORD']
        
        # Determinar el nombre final de la DB (usa el override o el default)
        alias_config = config['MONGO_DBS_ALIAS'].get(alias, {})
        db_name = alias_config.get('DB_NAME_OVERRIDE') or config['DB_NAME']
        
        # Construir la URI
        mongo_auth = f'{db_user}:{db_pass}@' if db_user and db_pass else ''
        return f'mongodb://{mongo_auth}{db_host}:{db_port}/{db_name}?authSource=admin'


    def get_client(self, db_alias='default'):
        """
        Obtiene un cliente de MongoDB por alias.
        Si no existe, intenta crearlo. Simula la logica de reconexion/failover.
        """
        logger = current_app.logger
        try:
            client = self.clients[db_alias]
            client.admin.command('ping') # Verificar conexion
            return client
        except (KeyError, pymongo.errors.ConnectionFailure):
            # Si la conexion falla, intenta reconectar/conectar
            try:
                uri = self._build_uri(db_alias)
                logger.info(f'Connecting to MongoDB with alias: {db_alias}')

                # Crear cliente
                new_client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
                new_client.admin.command('ping')

                self.clients[db_alias] = new_client
                return new_client

            except Exception as e:
                logger.error(f'Failed to connect to MongoDB alias {db_alias}: {e}')
                raise RuntimeError(f'Failed to connect to MongoDB alias {db_alias}: {e}')


    def get_db(self, db_alias='default', db_name=None):
        """
        Devuelve un objeto de Base de Datos especifico.
        """
        client = self.get_client(db_alias)

        if db_name is None:
            config = current_app.config
            alias_config = config['MONGO_DBS_ALIAS'].get(db_alias, {})
            db_name = alias_config.get('DB_NAME_OVERRIDE') or config['DB_NAME']

        return client[db_name]
