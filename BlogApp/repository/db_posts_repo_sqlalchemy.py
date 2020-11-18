from injector import inject
#from sqlalchemy import text
from flask import session
from sqlalchemy.orm import Session
from setup.db_connect import DbConnect
from repository.models.post import Post
from repository.models.user import User
from repository.posts_repo import PostsRepo

class DbPostsRepoSqlalchemy(PostsRepo):

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.session = Session(bind=self.db_connect.get_engine())

    def find_by_id(self, pid):
        post = self.session.query(Post.post_id, Post.title, User.name, \
            Post.contents, Post.created_at).join(User).filter(Post.post_id == '{}'.format(pid))
        return post

    def find_by_id2(self, pid):
      
        sql = text('SELECT post_id, title, owner, name, contents, posts.created_at,\
                posts.modified_at FROM posts INNER JOIN users\
                ON owner = user_id WHERE post_id=:x')
        result = self.db_connect.conn.execute(sql, x = '{}'.format(pid))

        row = result.fetchone()
        post = Post.get_post(row)

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
        self.db_connect.conn.execute(sql, record_to_update)

    def delete(self, pid):
        sql = "DELETE FROM posts WHERE post_id=%s"
        self.db_connect.conn.execute(sql, (pid, ))

    def add(self, post):
        #self.session = Session(bind=self.db_connect.get_engine())
        self.session.add(post)
        self.session.commit()


    def get_all(self, owner_id=0, records_per_page='all', offset=0):
        pass

    def get_count(self, owner_id=0):
        pass
