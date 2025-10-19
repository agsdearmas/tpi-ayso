

# Configuraciones de bases Mongo por alias
class MongoConfig:
    MONGO_DBS_ALIAS = {
        'default': {
            'DB_NAME_OVERRIDE': None, # Utiliza el nombre de db global definido en settings
        },
        'develop': {
            'DB_NAME_OVERRIDE': 'dev_habit-tracker',
        },
        'staging': {
            'DB_NAME_OVERRIDE': 'stg_habit-tracker',
        },
        'testing': {
            'DB_NAME_OVERRIDE': 'test_habit-tracker',
        },
    }
