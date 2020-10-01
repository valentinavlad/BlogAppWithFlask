import psycopg2
from repository.interface_posts_repo import InterfacePostRepo
from setup.config import config
from models.post import Post
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
    def transfrom_row_in_post(self, row):
        post_id = row[0]
        title = row[1]
        owner = row[2]
        contents = row[3]
        created_at = row[4]
        modified_at = row[5]
        post = Post(title,owner,contents)
        post.created_at = created_at
        post.modified_at = modified_at
        return post

    def view_posts(self):
        conn = None
        posts = []
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM posts ORDER BY created_at")
            #data = cur.fetchall()
            #print(data)
            #print(type(data))
            print("The number of parts: ", cur.rowcount)
            row = cur.fetchone()
        
            while row is not None:
                post = self.transfrom_row_in_post(row)
                posts.append(post)

                row = cur.fetchone()
       
            cur.close()
            return posts
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
