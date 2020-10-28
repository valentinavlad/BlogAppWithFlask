from injector import inject
from setup.db_connect import DbConnect

FILENAME = 'queries.sql'
class DbOperations:
    version = 1

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.filename = FILENAME

    def create_database(self, database_name):
        self.db_connect.autocommit = True
        cur = self.db_connect.conn.cursor()
        cur.execute('CREATE DATABASE {};'.format(database_name))
        cur.close()
        self.db_connect.conn.close()
        self.execute_scripts_from_file()

    def execute_scripts_from_file(self):
        cursor = self.db_connect.conn.cursor()
        filename = 'queries.sql'
        file = open('scripts/{}'.format(filename), 'r')
        sql_file = file.read()
        file.close()
        sql_commands = sql_file.split(';')
        for command in sql_commands:
            #cls.db_connect.conn = cls.db_connect.connect_to_db()
            if command not in ('', '\\n'):
                cursor.execute(command)
            else:
                continue
        cursor.close()
        self.db_connect.conn.commit()
        self.version += 1

    def check_version(self):
        config_params = self.db_connect.config.load()
        if int(config_params['version']) < self.version:
            self.execute_scripts_from_file()
            config_params.version = self.version

    def check_database(self):
        params = self.db_connect.config.load()
        database_name = params['database']
        self.db_connect.connect_to_db()
        if self.db_connect.conn is not None:
            self.db_connect.conn.autocommit = True
            #cur = cls.db_connect.get_cursor()
            cur = self.db_connect.conn.cursor()
            cur.execute("SELECT datname FROM pg_database;")
            list_database = cur.fetchall()
            if (database_name,) in list_database:
                self.check_version()
            else:
                self.create_database(database_name)
