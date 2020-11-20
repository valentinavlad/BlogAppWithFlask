import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from setup.database_config import DatabaseConfig

Base = declarative_base()

class DbConnect:
    def __init__(self):
        self.conn = None
        print(self.conn)
        print('DB connect')

    config = DatabaseConfig()

    def get_engine(self):
        db_credentials = self.config.load_configuration()
        params = db_credentials.to_dictionary()
        connection = 'postgres+psycopg2://{}:{}@{}:{}/{}'
        engine = create_engine(connection.format(params['user'], params['password'],\
            params['host'], params['port'], params['database']), echo=True)
        self.conn = engine.connect()
        return engine
