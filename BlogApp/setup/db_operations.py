from injector import inject
from setup.db_connect import DbConnect

FILENAME = 'queries.sql'
VERSION = 1
class DbOperations:

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.filename = FILENAME

    def is_db_updated(self):
        return self.db_connect.config.get_version() == VERSION

    def execute_scripts_from_file(self):
        if self.db_connect.conn is not None:
            file = open('scripts/{}'.format(self.filename), 'r')
            sql_file = file.read()
            file.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                if command not in ('', '\\n'):
                    self.db_connect.conn.execute(command)
                else:
                    continue

        self.db_connect.config.update_version(VERSION)

    def update_version(self):
        self.execute_scripts_from_file()
        self.db_connect.config.update_version(VERSION)

    def create_database(self):
        if self.db_connect.config.is_configured:
            if self.db_connect.conn is not None:
                params = self.db_connect.config.params
                database_name = params['database']
                self.db_connect.conn.execute('CREATE DATABASE IF NOT EXISTS {};'\
                    .format(database_name))
                self.update_version()
