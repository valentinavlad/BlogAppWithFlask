import psycopg2
from setup.config import Config

class DbOperations():
    conn = None
    config = Config()

    @classmethod
    def connect(cls):
        params = cls.config.config()
        return psycopg2.connect(**params)

    @classmethod
    def get_cursor(cls):
        cls.conn = cls.connect()
        return cls.conn.cursor()

    @classmethod
    def create_table(cls):
        """ create tables in the PostgreSQL database"""
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
        conn = None
        try:
            # read the connection parameters
            params = cls.config.config()
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
