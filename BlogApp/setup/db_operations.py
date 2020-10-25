import os
import psycopg2
from setup.database_config import DatabaseConfig

class DbOperations():
    conn = None
    config = DatabaseConfig()

    @classmethod
    def connect(cls):
        db_credentials = cls.config.load_configuration()
        params = db_credentials.to_dictionary()
        print("In connect function")
        return psycopg2.connect(**params)

    @classmethod
    def get_cursor(cls):
        cls.conn = cls.connect()
        return cls.conn.cursor()

    @staticmethod
    def read_all_sql_files_from_scripts():
        sql_files = []
        files = os.listdir('./scripts')
        for file in files:
            if file.endswith('.sql'):
                sql_files.append(file)
        print(sql_files)
        return sql_files

    @classmethod
    def create_database(cls, database_name):
        cls.conn.autocommit = True
        cur = cls.conn.cursor()
        cur.execute('CREATE DATABASE {};'.format(database_name))
        cur.close()
        cls.conn.close()
        cls.execute_scripts_from_file()
        #cls.scriptexecution('scripts/{}'.format('1_create_posts_table.sql'))

    @classmethod
    def execute_scripts_from_file(cls):
        file_list = cls.read_all_sql_files_from_scripts()

        for filename in file_list:
            file = open('scripts/{}'.format(filename), 'r')
            sql_file = file.read()
            file.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                cls.conn = cls.connect()
                cursor = cls.conn.cursor()
                if command not in ('', '\\n'):
                    cursor.execute(command)
                else:
                    continue
                cursor.close()
                cls.conn.commit()
    @classmethod
    def connect_to_db(cls):
        params = cls.config.load()
        database_name = params['database']
        try:
            cls.conn = psycopg2.connect(host=params['host'], port=params['port'],
                                        user=params['user'], password=params['password'])
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
            cls.conn = None

        if cls.conn is not None:
            #verify if db exists
            cls.conn.autocommit = True
            cur = cls.conn.cursor()
            cur.execute("SELECT datname FROM pg_database;")
            list_database = cur.fetchall()
            if (database_name,) in list_database:
                print("'{}' Database already exist".format(database_name))
                #check db version???????
                cls.execute_scripts_from_file()
            else:
                cls.create_database(database_name)
                print("'{}' Database not exist.".format(database_name))
