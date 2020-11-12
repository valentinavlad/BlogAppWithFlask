import math
class Pagination:
    records_per_page = 5
    first_page = 1

    def __init__(self, current_page, count):
        self.current_page = current_page
        self.count = count

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
