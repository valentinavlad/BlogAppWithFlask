import psycopg2
from models.post import Post

class Pagination:
    records_per_page = 3
    first_page = 1
    def __init__(self, current_page, repo):
        self.current_page = current_page
        self.repo = repo

    @property
    def next_page(self):
        return self.current_page + 1

    @property
    def prev_page(self):
        return self.current_page - 1 if self.current_page > self.first_page else None

    def get_offset(self, current_page):
        return (current_page - 1) * self.records_per_page

    def has_next(self):
        offset = self.get_offset(self.next_page)
        return True if self.repo.get_all_by_offset(self.records_per_page, offset) is not None else False

    def has_prev(self):
        if self.prev_page is not None:
            offset = self.get_offset(self.prev_page)
            return True if self.repo.get_all_by_offset(self.records_per_page, offset) is not None else False
        else:
            return False

    def get_posts_paginated(self):
        posts = []
        offset = self.get_offset(self.current_page)
        posts = self.repo.get_all_by_offset(self.records_per_page, offset)
        return posts

