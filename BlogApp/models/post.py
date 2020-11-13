import datetime
from flask import session
class Post():
    count = 1
    def __init__(self, title, owner, contents):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        Post.count += 1

    @classmethod
    def get_post(cls, row):
        cls.post_id = row[0]
        cls.title = row[1]
        cls.owner = row[2]
        cls.name = row[3]
        cls.contents = row[4]
        cls.created_at = row[5]
        cls.modified_at = row[6]
        obj = cls(cls.title, cls.owner, cls.contents)
        obj.created_at = cls.created_at.strftime("%b %d %Y %H:%M:%S")
        obj.modified_at = cls.modified_at
        obj.post_id = cls.post_id
        obj.name = cls.name
        return obj

    def is_owner(self):
        return int(self.owner) == session['user_id']

    def is_admin(self):
        return self.is_owner() and session['name'] == 'admin'

    def __str__(self):
        return self.title + " " + self.owner

    __repr__ = __str__
