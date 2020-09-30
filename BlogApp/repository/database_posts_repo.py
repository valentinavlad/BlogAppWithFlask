from repository.interface_posts_repo import InterfacePostRepo
import psycopg2

class DatabasePostRepo(InterfacePostRepo):
    """description of class"""
    def __init__(self):
        pass
    def add(self):
        sql = "INSERT INTO posts(title, owner,contents,created_at,modified_at) VALUES(%s,%s,%s,%s,%s)"
        # ??? 
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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()