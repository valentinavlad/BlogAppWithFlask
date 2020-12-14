import datetime
import json
from flask import session

class Post(object):
    count = 1
    def __init__(self, title, owner, contents):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        self.img = None
        Post.count += 1

    @classmethod
    def unmapp_post(cls, post_repo):
        cls.post_id = post_repo.post_id
        cls.title = post_repo.title
        cls.owner = post_repo.owner
        cls.contents = post_repo.contents
        cls.created_at = post_repo.created_at
        cls.modified_at = post_repo.modified_at
        cls.name = post_repo.name
        cls.img = post_repo.image
        obj = cls(cls.title, cls.owner, cls.contents)
        obj.post_id = cls.post_id
        obj.created_at = cls.created_at.strftime("%d %B %Y")
        obj.img = cls.img
        obj.name = cls.name
        return obj

    def is_owner(self):
        return int(self.owner) == session['user_id']

    def is_admin(self):
        return self.is_owner() and session['name'] == 'admin'

    def __str__(self):
        return self.title + " " + self.name

    __repr__ = __str__
