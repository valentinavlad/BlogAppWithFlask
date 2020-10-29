from injector import inject
from setup.db_connect import DbConnect

FILENAME = 'queries.sql'
VERSION = 1
class DbOperations:
   
    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.filename = FILENAME

    def create_database(self, database_name):
        self.db_connect.autocommit = True
        cur = self.db_connect.conn.cursor()
        cur.execute('CREATE DATABASE {};'.format(database_name))
        cur.close()
        #self.db_connect.conn.close()
        self.execute_scripts_from_file()

        self.db_connect.config.update_version(VERSION)        

    def execute_scripts_from_file(self):
        try:
            self.db_connect.conn = self.db_connect.connect() 
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        if self.db_connect.conn is not None:
            filename = 'queries.sql'
            file = open('scripts/{}'.format(filename), 'r')
            sql_file = file.read()
            file.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                cursor = self.db_connect.conn.cursor()
                cur = self.db_connect.get_cursor()
                if command not in (''):
                    cur.execute(command)
                else:
                    continue
                cur.close()
                self.db_connect.conn.commit()

    def check_version(self):
        config_version = self.db_connect.config.get_version()
        if config_version < VERSION:
            self.db_connect.conn.close()
            self.execute_scripts_from_file()
            self.db_connect.config.update_version(VERSION)

    def check_database(self):
        if self.db_connect.config.is_configured:
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
