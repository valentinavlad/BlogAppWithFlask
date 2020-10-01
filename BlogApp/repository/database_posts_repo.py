import psycopg2
from repository.interface_posts_repo import InterfacePostRepo
from setup.config import config

class DatabasePostRepo(InterfacePostRepo):
    def __init__(self):
        pass
    def find_post_id(self, pid):
        pass
    def edit_post(self, post):
        pass
    def delete_post(self, pid):
        pass

    def add_post(self, post):
        pass
    def view_posts(self):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM posts ORDER BY created_at")
            print("The number of parts: ", cur.rowcount)
            row = cur.fetchone()

            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
