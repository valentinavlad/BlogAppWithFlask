import psycopg2
from repository.posts_repo import PostsRepo
from models.post import Post
from setup.db_operations import DbOperations

class DatabasePostRepo(PostsRepo):
    db_operations = DbOperations()
    def __init__(self):
        pass

    def find_post_id(self, pid):
        try:
            cur = self.db_operations.get_cursor()
            sql = "SELECT * FROM posts WHERE post_id=%s"
            cur.execute(sql, (pid,))
            row = cur.fetchone()
            post = Post.get_post(row)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return post

    def edit_post(self, post):
        sql = """UPDATE posts
                    SET title=%s, owner=%s,
                    contents=%s,
                    created_at=%s,
                    modified_at=%s
                    WHERE post_id=%s"""
        record_to_update = (post.title, post.owner, post.contents,
                            post.created_at, post.modified_at, post.post_id)
        try:
            cur = self.db_operations.get_cursor()
            cur.execute(sql, record_to_update)
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()

    def delete_post(self, pid):
        try:
            cur = self.db_operations.get_cursor()
            sql = "DELETE FROM posts WHERE post_id=%s"
            cur.execute(sql, (pid, ))
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()

    def add_post(self, post):
        sql = """INSERT INTO posts(title, owner,contents,
                        created_at,modified_at)
                 VALUES(%s,%s,%s,%s,%s) RETURNING post_id;"""
        record_to_insert = (post.title, post.owner, post.contents,
                            post.created_at, post.modified_at)
        post_id = None
        try:
            cur = self.db_operations.get_cursor()
            cur.execute(sql, record_to_insert)
            post_id = cur.fetchone()[0]
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return post_id

    def view_posts(self):
        posts = []
        try:
            cur = self.db_operations.get_cursor()
            cur.execute("SELECT * FROM posts ORDER BY created_at desc")
            row = cur.fetchone()
            while row is not None:
                post = Post.get_post(row)
                posts.append(post)
                row = cur.fetchone()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return posts
