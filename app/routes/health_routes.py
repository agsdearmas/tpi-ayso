import traceback
import pymongo.errors
from flask import Blueprint, jsonify
from flask import current_app
from app.services.mongo_manager.db_service import MongoService


health_bp = Blueprint('health_bp', __name__, url_prefix='/healthcheck')

@health_bp.route('/mongo', methods=['GET'])
def mongo_healthcheck():
    try:
        # Obtener instancia del servicio y conexion a la DB
        mongo_service = current_app.mongo_service
        db = mongo_service.get_db(alias='default')

        # Ejecutar una operacion ligera adicional para mayor seguridad
        collection_names = db.list_collection_names()

        return jsonify({
            'status': 200,
            'message': 'MongoDB connection is successful (default alias)',
            'db_name': db.name,
            'collections_count': len(collection_names)
        }), 200
    
    except pymongo.errors.ConnectionFailure as e:
        # Error especifico de conexion a MongoDB (Service Unavailable)
        return jsonify({
            'status': 503,
            'message': f'MongoDB connection FAILED for alias "default": {e}'
        }), 503
    
    except Exception as e:
        # Errores de configuracion, inicializacion, etc (Internal Server Error)
        full_traceback = traceback.format_exc()
        current_app.logger.error(f'Health Check Error: {e}\n{full_traceback}')

        return jsonify({
            'status': 500,
            'message': f'Internal Server Error during health check: {e}'
        }), 500
