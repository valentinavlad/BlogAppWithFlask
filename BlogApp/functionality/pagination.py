from injector import inject
import psycopg2
from models.post import Post
from setup.db_connect import DbConnect
from repository.posts_repo import PostsRepo

class Pagination(DbConnect):
    records_per_page = 3
    first_page = 1
    def __init__(self, current_page):
        self.current_page = current_page
        super().__init__()

    @property
    def next_page(self):
        return self.current_page + 1

    @property
    def prev_page(self):
        return self.current_page - 1 if self.current_page > self.first_page else None

    def get_offset(self, current_page):
        return (current_page - 1) * self.records_per_page

    def has_next(self):
        offset = self.get_offset(self.next_page)
        return True if self.get_posts(offset) is not None else False

    def has_prev(self):
        if self.prev_page is not None:
            offset = self.get_offset(self.prev_page)
            return True if self.get_posts(offset) is not None else False
        else:
            return False

    def get_posts(self, offset):
        cur = super().get_cursor()
        sql2 = """SELECT post_id, title, owner, name, contents, posts.created_at,\
                         posts.modified_at FROM posts INNER JOIN users \
                         ON owner = user_id ORDER BY created_at desc LIMIT {} OFFSET {}"""
        cur.execute(sql2.format(self.records_per_page, offset))
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_posts_paginated(self):
        posts = []
        offset = self.get_offset(self.current_page)
        try:
           rows = self.get_posts(offset)
           for row in rows:
               post = Post.get_post(row)
               posts.append(post)
          
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
          
        return posts
