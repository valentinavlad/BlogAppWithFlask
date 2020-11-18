import psycopg2
from injector import inject
from flask import session
from sqlalchemy.orm import Session
from setup.db_connect import DbConnect
from repository.models.post import Post
from repository.models.user import User
from repository.posts_repo import PostsRepo
from models.post import Post as ModelPost

class DbPostsRepoSqlalchemy(PostsRepo):

    @inject
    def __init__(self, db_connect: DbConnect):
        self.db_connect = db_connect
        self.session = Session(bind=self.db_connect.get_engine())

    def find_by_id(self, pid):
        result = self.session.query(Post.post_id, Post.title, Post.owner, User.name, \
            Post.contents, Post.created_at, Post.modified_at)\
            .join(User).filter(Post.post_id == '{}'.format(pid)).first()

        result_to_list = ModelPost.get_list_from_result(result)
        return ModelPost.get_post(result_to_list)

    def edit(self, post):
        post_update = {Post.title: post.title, Post.owner: session['user_id'],
                       Post.contents: post.contents, Post.created_at: post.created_at,
                       Post.modified_at: post.modified_at}
        get_post = self.session.query(Post).filter(Post.post_id == post.post_id)
        get_post.update(post_update)
        self.session.commit()

    def delete(self, pid):
        post = self.session.query(Post).filter(Post.post_id == pid).first()
        self.session.delete(post)
        self.session.commit()

    def add(self, post):
        self.session.add(post)
        self.session.commit()

    def get_all(self, owner_id=0, records_per_page='all', offset=0):
        posts = []
        where_clause = "WHERE posts.owner = {}" if owner_id != 0 else " "
        check_owner = where_clause.format(owner_id)
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
                post = ModelPost.get_post(row)
                posts.append(post)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

        return posts

    def get_count(self, owner_id=0):
        where_clause = ' where posts.owner = {}' if owner_id != 0 else " "
        check_owner = where_clause.format(owner_id)
        sql = "SELECT count(*) from posts {};"
        cur = self.db_connect.get_cursor()
        cur.execute(sql.format(check_owner))
        row = cur.fetchone()
        cur.close()

        return row[0]
