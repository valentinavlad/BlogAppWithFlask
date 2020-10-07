import psycopg2
from setup.config import Config

# import sys to get more detailed Python exception info
import sys



# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors




class DbOperations():
    conn = None
    config = Config()

    @classmethod
    def connect(cls):
        params = cls.config.config()
        print("In connect function")
        return psycopg2.connect(**params)

    @classmethod
    def get_cursor(cls):
        cls.conn = cls.connect()
        return cls.conn.cursor()

    @classmethod
    def check_table_exists(cls):
        cur = cls.conn.cursor()
        isTable = cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('posts',))
        
        if isTable is None:
            cur.close()
            cls.conn.close()
            cls.create_table()
            cls.conn = None
        else:
           cur.close()
           cls.conn.close()

    @classmethod
    def create_database(cls, database_name):
        cls.conn.autocommit = True
        cur = cls.conn.cursor()
        cur.execute('CREATE DATABASE {};'.format(database_name))
        cur.close()
        cls.conn.close()
        cls.create_table()

    @classmethod
    def connect_to_db(cls):
        params = cls.config.config()
        database_name = params['database']
        try:
            cls.conn = psycopg2.connect(host=params['host'], port=params['port'],
                        user=params['user'], password=params['password'])      
        except OperationalError as err:
            # pass exception to function
            print_psycopg2_exception(err)
            cls.conn = None
             
        if cls.conn is not None:
            #verify if db exists
            cls.conn.autocommit = True
            cur = cls.conn.cursor()
            cur.execute("SELECT datname FROM pg_database;")
            list_database = cur.fetchall()
            if (database_name,) in list_database:
                print("'{}' Database already exist".format(database_name))
                cls.check_table_exists() 
            else:
                cls.create_database(database_name)
                print("'{}' Database not exist.".format(database_name))

    @classmethod
    def create_table(cls):
        command = """
            CREATE TABLE posts (
                post_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                owner VARCHAR(255) NOT NULL,
                contents Text NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                modified_at DATE NULL
                )
            """
        try:
            cls.conn = cls.connect()
            cur = cls.conn.cursor()
            # create table
            cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            cls.conn.commit()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cls.conn is not None:
                cls.conn.close()
    #TO DO move in other class
    def print_psycopg2_exception(err):
        err_type, err_obj, traceback = sys.exc_info()
        # get the line number when exception occured
        line_num = traceback.tb_lineno
        # print the connect() error
        print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
        print ("psycopg2 traceback:", traceback, "-- type:", err_type)

        # psycopg2 extensions.Diagnostics object attribute
        print ("\nextensions.Diagnostics:", err.diag)

        # print the pgcode and pgerror exceptions
        print ("pgerror:", err.pgerror)
        print ("pgcode:", err.pgcode, "\n")
