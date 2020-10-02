class Post():
    count = 1

    def __init__(self,title,owner,contents, created_at,modified_at):
        self.post_id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at =  created_at
        self.modified_at = modified_at
        Post.count += 1
    def __str__(self):
        return self.title + " " + self.owner

    __repr__ = __str__
