import datetime
class Post():
    count = 1
    date_now = datetime.datetime.now()
    def __init__(self, title, owner, contents):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        Post.count += 1
        #ar trebui sa  adaug si user_id aici
    @classmethod
    def get_post(cls, row):
        cls.post_id = row[0]
        #cls.user_id = row[1]
        cls.title = row[2]
        cls.owner = row[3]
        cls.contents = row[4]
        cls.created_at = row[5]
        cls.modified_at = row[6]
        obj = cls(cls.title, cls.owner, cls.contents)
        obj.created_at = cls.created_at
        obj.modified_at = cls.modified_at
        obj.post_id = cls.post_id
        return obj

    def __str__(self):
        return self.title + " " + self.owner

    __repr__ = __str__
