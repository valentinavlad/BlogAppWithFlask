import psycopg2
from setup.config import Config

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
    def create_database(cls):
        print("@@@@@@@@@@")
        params = cls.config.config()

        try:      
            print('Connecting to the PostgreSQL database...')
            cls.conn = psycopg2.connect(host=params['host'], port=params['port'],
                                          user=params['user'], password=params['password'])
            print("Database connected")
        except:
             print('Database not connected.')
        if cls.conn is not None:
            cls.conn.autocommit = True
            cur = cls.conn.cursor()
            database_name = params['database']
            cur.execute('CREATE DATABASE {};'.format(database_name))
	        # close the communication with the PostgreSQL
            cur.close()
            cls.conn.close()
            cls.create_table()

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
