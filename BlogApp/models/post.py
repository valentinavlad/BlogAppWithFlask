import datetime
from flask import session
class Post():
    count = 1
    def __init__(self, title, owner, contents, img=None):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        self.img = img
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
        cls.img = row[7]
        obj = cls(cls.title, cls.owner, cls.contents, cls.img)
        obj.created_at = cls.created_at.strftime("%b %d %Y %H:%M:%S")
        obj.modified_at = cls.modified_at
        obj.post_id = cls.post_id
        obj.name = cls.name
        return obj
    
    @classmethod
    def unmapp_post(cls, post_repo):
        cls.post_id = post_repo.post_id
        cls.title = post_repo.title
        cls.owner = post_repo.owner
        cls.contents = post_repo.contents
        cls.created_at = post_repo.created_at
        cls.modified_at = post_repo.modified_at
        cls.img = post_repo.image
        obj = cls(cls.title, cls.owner, cls.contents, cls.img)
        obj.post_id = cls.post_id
        return obj

    @staticmethod
    def get_list_from_result(result):
        list_dict = []
        for i in result:
            list_dict.append(i)
        return list_dict

    def is_owner(self):
        return int(self.owner) == session['user_id']

    def is_admin(self):
        return self.is_owner() and session['name'] == 'admin'

    def __str__(self):
        return self.title + " " + self.name

    __repr__ = __str__
