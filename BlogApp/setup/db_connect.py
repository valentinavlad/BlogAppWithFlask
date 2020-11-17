#import psycopg2
from sqlalchemy import create_engine
from setup.database_config import DatabaseConfig

class DbConnect:

    def __init__(self):
        self.conn = self.get_engine().connect()
        print(self.conn)
        print('DB connect')
    config = DatabaseConfig()

    def get_engine(self):
        db_credentials = self.config.load_configuration()
        params = db_credentials.to_dictionary()
        connection = 'postgres+psycopg2://{}:{}@{}:{}/{}'
        return create_engine(connection.format(params['user'], params['password'],\
           params['host'], params['port'], params['database']), echo=True)
