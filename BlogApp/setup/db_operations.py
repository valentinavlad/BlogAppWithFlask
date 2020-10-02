import psycopg2
from setup.config import config

class DbOperations(object):
    conn = None

    @classmethod
    def connect(cls):
        params = config()
        return psycopg2.connect(**params)

    @classmethod
    def get_cursor(cls):
        cls.conn = cls.connect()
        #return conn.cursor() if cls.conn is not None  else None
        return cls.conn.cursor()
    
    def create_table():
        """ create tables in the PostgreSQL database"""
        command = """
            CREATE TABLE posts (
                post_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                owner VARCHAR(255) NOT NULL,
                contents VARCHAR(255) NOT NULL,
                created_at DATE NOT NULL DEFAULT CURRENT_DATE,
                modified_at DATE NULL
                )
            """
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # create table
            cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


