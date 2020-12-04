from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from setup.database_config import DatabaseConfig

Base = declarative_base()

class DbConnect:
    config = DatabaseConfig()
    def __init__(self):
        self.Session = sessionmaker()   
        print("dbconnect")


    def get_engine(self):
        connection = None
        if self.config.is_configured():
            connection = 'postgres+psycopg2://{}:{}@{}:{}/{}'.\
                          format(self.config.params['user'], self.config.params['password'],\
                          self.config.params['host'], self.config.params['port'],\
                          self.config.params['database'])
        engine = create_engine(connection, echo=True, isolation_level="AUTOCOMMIT")
        self.Session.configure(bind=engine)
        return engine

    def get_engine_create_db(self):
        connection = None
        if self.config.is_configured():
            connection = 'postgres+psycopg2://{}:{}@{}:{}'.\
                          format(self.config.params['user'], self.config.params['password'],\
                          self.config.params['host'], self.config.params['port'])
        engine = create_engine(connection, echo=True, isolation_level="AUTOCOMMIT")
        self.Session.configure(bind=engine)
        return engine
