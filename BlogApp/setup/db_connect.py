import psycopg2
from sqlalchemy import create_engine
from setup.database_config import DatabaseConfig

class DbConnect:

    config = DatabaseConfig()

    def connect(self):
        db_credentials = self.config.load_configuration()
        params = db_credentials.to_dictionary()
        connection = 'postgres+psycopg2://{}:{}@{}:{}/{}'
        #conn = engine.connect()
        return create_engine(connection.format(params['user'], params['passwoed'], params['host'], params['port'], params['database']), echo=True)
