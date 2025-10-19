from app.services.mongo_manager import db_service


services = [
    db_service.MongoService(),
]
