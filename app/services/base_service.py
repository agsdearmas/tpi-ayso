

class BaseService:
    """
    Clase base para inicializar todos los servicios dentro del core.
    """
    def init_app(self, app):
        raise NotImplementedError('Cada servicio debe implementar init_app()')
