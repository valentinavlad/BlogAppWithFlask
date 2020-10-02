import psycopg2
from repository.interface_posts_repo import InterfacePostRepo
from setup.config import config
from models.post import Post
class DatabasePostRepo(InterfacePostRepo):
    def __init__(self):
        pass
    def transfrom_row_in_post(self, row):
        post_id = row[0]
        title = row[1]
        owner = row[2]
        contents = row[3]
        created_at = row[4]
        modified_at = row[5]
        post = Post(title,owner,contents, created_at, modified_at)
        post.post_id = post_id
        return post

    def find_post_id(self, pid):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            sql = "SELECT * FROM posts WHERE post_id=%s"
            cur.execute(sql, (pid,))
            row = cur.fetchone()
            post = self.transfrom_row_in_post(row)
            count = cur.rowcount
            print(count, "Post was found ")
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return post
    def edit_post(self, post):
        sql = """UPDATE posts
                    SET title=%s, owner=%s, contents=%s,  created_at=%s,
                    modified_at=%s
                    WHERE post_id=%s"""
        record_to_update = (post.title, post.owner, post.contents,
                            post.created_at, post.modified_at,post.post_id)
        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute(sql, record_to_update)
            # Commit the changes to the database
            conn.commit()
            # Close communication with the PostgreSQL database
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    def delete_post(self, pid):
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            sql = "DELETE FROM posts WHERE post_id=%s"
            cur.execute(sql, (pid, ))
            conn.commit()
            count = cur.rowcount
            print(count, "Record deleted successfully ")
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def add_post(self, post):
        sql = """INSERT INTO posts(title, owner,contents,created_at,modified_at)
                 VALUES(%s,%s,%s,%s,%s) RETURNING post_id;"""
        record_to_insert = (post.title, post.owner, post.contents,
                            post.created_at, post.modified_at)
        conn = None
        post_id = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, record_to_insert)
            post_id = cur.fetchone()[0]
            conn.commit()
            count = cur.rowcount
            print (count, "Record inserted successfully into posts table")
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return post_id

    def view_posts(self):
        conn = None
        posts = []
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM posts ORDER BY created_at desc")
            row = cur.fetchone()
            while row is not None:
                post = self.transfrom_row_in_post(row)
                posts.append(post)
                row = cur.fetchone()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return posts
