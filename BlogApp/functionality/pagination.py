from injector import inject
from repository.posts_repo import PostsRepo

class Pagination:
    @inject
    def __init__(self, repo: PostsRepo):
        self.repo = repo

    current_page = 1
    records_per_page = 3
    limit_optional_offset = (current_page - 1) * records_per_page

    def count_all_posts(self):
        return len(self.repo.view_all)
    def get_all_posts(self, page_number, page_size, sort_order):
        pass
