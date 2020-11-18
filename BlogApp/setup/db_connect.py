from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from setup.database_config import DatabaseConfig

Base = declarative_base()

class DbConnect:
    config = DatabaseConfig()
    def __init__(self):
        self.conn = self.get_engine().connect()
        print(self.conn)
        print('DB connect')


    def get_engine(self):
        db_credentials = self.config.load_configuration()
        params = db_credentials.to_dictionary()
        connection = 'postgres+psycopg2://{}:{}@{}:{}/{}'
        return create_engine(connection.format(params['user'], params['password'],\
           params['host'], params['port'], params['database']), echo=True)



    #engine = create_engine('postgres+psycopg2://{}:{}@{}:{}/{}'.format(config.params['user'],\
    #            config.params['password'], config.params['host'],\
    #            config.params['port'], config.params['database']))
