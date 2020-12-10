import math
class Pagination:
    records_per_page = 5
    first_page = 1

    def __init__(self):
        self._current_page = None
        self._count = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, page):
        if page is not None:
           self._current_page = page

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, get_count):
        if get_count is not None:
           self._count = get_count

    @property
    def pages(self):
        return int(math.ceil(self.count / float(self.records_per_page)))

    @property
    def next_page(self):
        return self.current_page + 1

    @property
    def offset(self):
        return (self.current_page - 1) * self.records_per_page

    @property
    def prev_page(self):
        return self.current_page - 1 if self.current_page > self.first_page else None

    def get_offset(self, current_page):
        return (current_page - 1) * self.records_per_page

    def has_next(self):
        return self.current_page < self.pages

    def has_prev(self):
        return self.prev_page is not None
