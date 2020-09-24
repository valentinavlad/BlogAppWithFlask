class Post():
    count = 1

    def __init__(self,title,owner,contents,created_at,modified_at):
        self.id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = created_at
        self.modified_at = modified_at
        Post.count += 1
