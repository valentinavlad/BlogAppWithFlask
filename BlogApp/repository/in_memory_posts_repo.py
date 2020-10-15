from repository.posts_data import dummy_posts
from repository.posts_repo import PostsRepo

class InMemoryPostsRepo(PostsRepo):
    def __init__(self):
        pass
    def find_by_id(self, pid):
        found_post = None
        for post in dummy_posts:
            if post.post_id == pid:
                found_post = post
        return found_post

    def view_all(self):
        return dummy_posts

    def edit(self, post):
        index = dummy_posts.index(post)
        dummy_posts[index] = post

    def delete(self, pid):
        post = self.find_by_id(pid)
        dummy_posts.remove(post)

    def add(self, post):
        dummy_posts.insert(0, post)
