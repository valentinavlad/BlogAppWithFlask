import psycopg2
from setup.config import Config

class DbOperations():
    conn = None
    config = Config()

    @classmethod
    def connect(cls):
        params = cls.config.save()
        print("In connect function")
        return psycopg2.connect(**params)

    @classmethod
    def get_cursor(cls):
        cls.conn = cls.connect()
        return cls.conn.cursor()

    @classmethod
    def check_table_exists(cls):
        cur = cls.conn.cursor()
        is_table = cur.execute("""select exists(
                               select * from
                               information_schema.tables
                               where table_name=%s)""", ('posts',))
        if is_table is None:
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
        params = cls.config.save()
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
            cur.execute(command)
            cur.close()
            cls.conn.commit()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cls.conn is not None:
                cls.conn.close()
