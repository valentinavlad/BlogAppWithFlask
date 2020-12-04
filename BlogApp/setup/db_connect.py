from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from setup.database_config import DatabaseConfig

Base = declarative_base()

class DbConnect:
    config = DatabaseConfig()
    def __init__(self):
        print("dbconnect")

    @property
    def connection(self):
        return 'postgres+psycopg2://{}:{}@{}:{}/{}'.\
                format(self.config.params['user'], self.config.params['password'],\
                self.config.params['host'], self.config.params['port'],\
                self.config.params['database'])
    @property
    def connection_to_server_pg(self):
        return 'postgres+psycopg2://{}:{}@{}:{}'.\
                format(self.config.params['user'], self.config.params['password'],\
                self.config.params['host'], self.config.params['port'])

    def get_engine(self):
        engine = create_engine(self.connection, echo=True, isolation_level="AUTOCOMMIT")
        return engine
