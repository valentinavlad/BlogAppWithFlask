from injector import inject
from itertools import islice
from flask import session
from repository.posts_repo import PostsRepo

class UserStatistic:
    @inject
    def __init__(self, repo: PostsRepo):
        self.repo = repo
        self.owner_id = 0 if session.get("user_id") is None else int(session['user_id'])

    @property
    def count_posts(self):
        return self.repo.get_count(self.owner_id)

    def get_user_posts(self):
        posts = self.repo.get_all(self.owner_id, self.count_posts, 0)
        statistics = {}
        for post in posts:
            get_date = post.created_at.split(' ')
            key = (get_date[2], get_date[1])
            if key in statistics:
                statistics[key].append(post)
            else:
                statistics[key] = [post]
        return statistics

    def get_all(self, records_per_page=3, offset=0):
        posts_dict = self.get_user_posts()
        posts = dict(islice(posts_dict.items(), offset, records_per_page + offset))
        return posts
