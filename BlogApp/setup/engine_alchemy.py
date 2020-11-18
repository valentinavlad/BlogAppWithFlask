from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setup.database_config import DatabaseConfig

config = DatabaseConfig()

engine = create_engine('postgres+psycopg2://{}:{}@{}:{}/{}'.format(config.params['user'],\
           config.params['password'], config.params['host'],\
           config.params['port'], config.params['database']))

Session = sessionmaker(bind=engine)

Base = declarative_base()
