from injector import inject
from flask import session as flask_session
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from sqlalchemy import or_, desc
from setup.db_connect import DbConnect
from repository.models.post import Post
from repository.models.user import User
from repository.posts_repo import PostsRepo
from repository.database_image_repo import DatabaseImageRepo
from models.post import Post as ModelPost

class DbPostsRepoSqlalchemy(PostsRepo):

    @inject
    def __init__(self, db_connect: DbConnect, db_image: DatabaseImageRepo):
        self.db_connect = db_connect
        self.db_image = db_image

    def find_by_id(self, pid):
        session = self.db_connect.session
        result = session.query(Post.post_id, Post.title, Post.owner, User.name, \
            Post.contents, Post.created_at, Post.modified_at, Post.image)\
            .join(User).filter(Post.post_id == '{}'.format(pid)).first()
        if result is None:
            return None
        post = ModelPost.unmapp_post(result)
        post.img = self.db_image.get(post.img)
        return post


    def edit(self, post):
        session = self.db_connect.session
        get_post = session.query(Post).filter(Post.post_id == post.post_id)
        unmap_post = ModelPost.unmapp_post(get_post.first())

        if isinstance(post.img, FileStorage):
            filename = self.db_image.edit(unmap_post.img, post.img)
            filename = secure_filename(filename)
        else:
            filename = unmap_post.img
        post_update = {Post.title: post.title, Post.owner: flask_session['user_id'],
                       Post.contents: post.contents, Post.created_at: post.created_at,
                       Post.modified_at: post.modified_at, Post.image: filename}
        get_post.update(post_update)
        session.commit()

    def delete(self, pid):
        session = self.db_connect.session
        post = session.query(Post).filter(Post.post_id == pid).first()
        filename = post.image
        session.delete(post)
        session.commit()
        self.db_image.delete(filename)

    def add(self, post):
        session = self.db_connect.session
        if post.img.filename == '':
            filename = '1.jpg'
        else:
            filename = self.db_image.add(post.img)
            filename = secure_filename(filename)
        post_to_add = Post(
            title=post.title,
            owner=post.owner,
            contents=post.contents,
            created_at=post.created_at,
            modified_at=post.modified_at,
            image=filename)

        session.add(post_to_add)
        session.commit()

    def get_all(self, owner_id=0, records_per_page='all', offset=0):
        session = self.db_connect.session
        query = session.query(Post.post_id, Post.title, Post.owner, User.name, \
            Post.contents, Post.created_at, Post.modified_at, Post.image).join(User)
        conditions = []
        if owner_id > 0:
            conditions.append(Post.owner == owner_id)
        query = query.filter(or_(*conditions))\
            .order_by(desc(Post.created_at))\
            .limit(records_per_page).offset(offset).all()

        posts = []

        for row in query:
            post = ModelPost.unmapp_post(row)
            post.img = self.db_image.get(post.img)
            posts.append(post)
        return posts

    def get_count(self, owner_id=0):
        session = self.db_connect.session
        query = session.query(Post.owner)
        conditions = []
        if owner_id > 0:
            conditions.append(Post.owner == owner_id)
        query = query.filter(or_(*conditions))
        count = query.count()
        return count
