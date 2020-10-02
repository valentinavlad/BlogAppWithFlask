class Post():
    count = 1

    def __init__(self,title,owner,contents,created_at,modified_at):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at =  created_at
        self.modified_at = modified_at
        Post.count += 1

    @classmethod
    def get_post(cls,row):
        cls.post_id = row[0]
        cls.title = row[1]
        cls.owner = row[2]
        cls.contents = row[3]
        cls.created_at = row[4]
        cls.modified_at = row[5]
        obj = cls(cls.title,cls.owner,cls.contents,cls.created_at,cls.modified_at)
        obj.post_id = cls.post_id
        return obj

    def __str__(self):
        return self.title + " " + self.owner

    __repr__ = __str__
