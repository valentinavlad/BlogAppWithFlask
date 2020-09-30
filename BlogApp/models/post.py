import datetime

class Post():
    count = 1

    date_now = datetime.datetime.now()
    created_at= date_now.strftime("%B %d, %Y")
    modified_at = date_now.strftime("%B %d, %Y")

    def __init__(self,title,owner,contents):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        Post.count += 1
    def __str__(self):
        return self.title + " " + self.owner

    __repr__ = __str__
