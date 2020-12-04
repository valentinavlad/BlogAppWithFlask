from injector import inject
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from setup.db_connect import DbConnect

FILENAME = 'queries.sql'
VERSION = 2
class DbOperations:

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.filename = FILENAME

    def is_db_updated(self):
        return self.db_connect.config.get_version() == VERSION

    def execute_scripts_from_file(self):
        engine = self.db_connect.get_engine()
        conn = engine.connect()
        file = open('scripts/{}'.format(self.filename), 'r')
        sql_file = file.read()
        file.close()
        sql_commands = sql_file.split(';')
        for command in sql_commands:
            if command not in ('', '\\n'):
                conn.execute("commit")
                conn.execute(command)
            else:
                continue
        conn.close()
        self.db_connect.config.update_version(VERSION)

    def update_version(self):
        self.execute_scripts_from_file()
        self.db_connect.config.update_version(VERSION)

    def create_database(self):
        if self.db_connect.config.is_configured:
            engine = self.db_connect.get_engine()
            if not database_exists(engine.url):
                engine = create_engine(self.db_connect.connection_to_server_pg,\
                   echo=True, isolation_level="AUTOCOMMIT")
                database_name = self.db_connect.config.params['database']
                conn = engine.connect()
                conn.execute("commit")
                conn.execute("create database {}".format(database_name))
                conn.close()
            else:
                engine.connect()
        self.update_version()
