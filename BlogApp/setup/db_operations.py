import psycopg2
from injector import inject
from setup.db_connect import DbConnect

FILENAME = 'queries.sql'
VERSION = 1
class DbOperations:

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.filename = FILENAME

    def check_owner_data_type(self):
        self.db_connect.connect_to_db()
        cur = self.db_connect.get_cursor()
        verify_owner_type_sql = "SELECT data_type FROM information_schema.columns\
                                 WHERE table_name = 'posts' AND column_name = 'owner';"
        cur.execute(verify_owner_type_sql)
        row = cur.fetchone()
        cur.close()
        self.db_connect.conn.close()
        return row

    def is_db_updated(self):
        return self.db_connect.config.get_version() == VERSION

    def execute_scripts_from_file(self):
        try:
            self.db_connect.conn = self.db_connect.connect()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        if self.db_connect.conn is not None:
            file = open('scripts/{}'.format(self.filename), 'r')
            sql_file = file.read()
            file.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                cur = self.db_connect.get_cursor()
                if command not in ('', '\\n'):
                    cur.execute(command)
                else:
                    continue
                cur.close()
                self.db_connect.conn.commit()
        self.db_connect.config.update_version(VERSION)

    def update_version(self):
        self.execute_scripts_from_file()
        self.db_connect.config.update_version(VERSION)

    def is_database_created(self, database_name):
        self.db_connect.conn.autocommit = True
        cur = self.db_connect.conn.cursor()
        cur.execute("SELECT datname FROM pg_database;")
        list_database = cur.fetchall()
        return (database_name,) in list_database

    def create_database(self):
        if self.db_connect.config.is_configured:
            self.db_connect.connect_to_db()
            if self.db_connect.conn is not None:
                params = self.db_connect.config.load()
                database_name = params['database']
                if not self.is_database_created(database_name):
                    self.db_connect.autocommit = True
                    cur = self.db_connect.conn.cursor()
                    cur.execute('CREATE DATABASE {};'.format(database_name))
                    cur.close()

                owner_type = self.check_owner_data_type()
                if owner_type is None or owner_type[0] == 'character varying':
                    self.update_version()
                if owner_type is not None and owner_type[0] == 'integer':
                    self.db_connect.config.update_version(VERSION)
            self.db_connect.conn.close()
