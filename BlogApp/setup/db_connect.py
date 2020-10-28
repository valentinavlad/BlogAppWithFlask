import psycopg2
from setup.database_config import DatabaseConfig

class DbConnect:
    conn = None

    config = DatabaseConfig()

    def connect(self):
        db_credentials = self.config.load_configuration()
        params = db_credentials.to_dictionary()
        return psycopg2.connect(**params)

    def get_cursor(self):
        self.conn = self.connect()
        return self.conn.cursor()

    def connect_to_db(self):
        params = self.config.load()
        try:
            self.conn = psycopg2.connect(host=params['host'], port=params['port'],
                                         user=params['user'], password=params['password'])
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
            self.conn = None
