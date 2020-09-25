from datetime import datetime

class Post():
    count = 1

    def __init__(self,title,owner,contents,created_at,modified_at):
        self.id = Post.count
        self.title = title
        self.owner = owner
        self.contents = contents
        self.created_at = datetime.strptime(created_at, "%B %d, %Y")
        self.modified_at = datetime.strptime(modified_at, "%B %d, %Y")
        Post.count += 1

