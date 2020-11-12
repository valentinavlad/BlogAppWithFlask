import psycopg2
from injector import inject
from flask import session
from repository.posts_repo import PostsRepo
from models.post import Post
from setup.db_connect import DbConnect

class DatabasePostRepo(PostsRepo):

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect

    def find_by_id(self, pid):
        try:
            cur = self.db_connect.get_cursor()
            sql = 'SELECT post_id, title, owner, name, contents, posts.created_at,\
                   posts.modified_at FROM posts INNER JOIN users\
                   ON owner = user_id WHERE post_id=%s'
            cur.execute(sql, (pid,))
            row = cur.fetchone()
            post = Post.get_post(row)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()
        return post

    def edit(self, post):
        sql = """UPDATE posts
                    SET title=%s, owner=%s,
                    contents=%s,
                    created_at=%s,
                    modified_at=%s
                    WHERE post_id=%s"""
        record_to_update = (post.title, session['user_id'], post.contents,
                            post.created_at, post.modified_at, post.post_id)
        try:
            cur = self.db_connect.get_cursor()
            cur.execute(sql, record_to_update)
            conn = self.db_connect.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

    def delete(self, pid):
        try:
            cur = self.db_connect.get_cursor()
            sql = "DELETE FROM posts WHERE post_id=%s"
            cur.execute(sql, (pid, ))
            conn = self.db_connect.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

    def add(self, post):
        sql = """INSERT INTO posts(title, owner,contents,
                        created_at,modified_at)
                 VALUES(%s,%s,%s,%s,%s) RETURNING post_id;"""
        record_to_insert = (post.title, post.owner, post.contents,
                            post.created_at, post.modified_at)
        post_id = None
        try:
            cur = self.db_connect.get_cursor()
            cur.execute(sql, record_to_insert)
            post_id = cur.fetchone()[0]
            conn = self.db_connect.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()
        return post_id

    def get_all(self, owner_id=0, records_per_page='all', offset=0):
        posts = []
        owner = "WHERE posts.owner = {}" if owner_id != 0 else " "
        check_owner = owner.format(owner_id)
        sql = """SELECT post_id, title, owner, name, contents, posts.created_at,
                            posts.modified_at FROM posts INNER JOIN users 
                            ON owner = user_id 
							{}
							ORDER BY created_at desc
							LIMIT {} OFFSET {};"""
        try:
            cur = self.db_connect.get_cursor()

            cur.execute(sql.format(check_owner, records_per_page, offset))
            rows = cur.fetchall()
            for row in rows:
                post = Post.get_post(row)
                posts.append(post)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

        return posts

    def get_count(self):
        sql = "SELECT count(*) from posts;"
        cur = self.db_connect.get_cursor()
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        return row[0]
