from itertools import islice
from injector import inject
from repository.posts_data import dummy_posts
from repository.posts_repo import PostsRepo
from repository.in_memory_users_repo import InMemoryUsersRepo

class InMemoryPostsRepo(PostsRepo):
    @inject
    def __init__(self, user_repo: InMemoryUsersRepo):
        self.user_repo = user_repo

    def find_by_id(self, pid):
        found_post = None
        for post in dummy_posts:
            if post.post_id == pid:
                found_post = post
        found_post.name = self.user_repo.find_by_id(int(found_post.owner)).name
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

    def get_all_by_offset(self, records_per_page=3, offset=0):
        posts = list(islice(dummy_posts, offset, records_per_page + offset))
        return posts
