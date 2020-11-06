class Pagination:
    current_page = 1
    records_per_page = 3
    limit_optional_offset = (current_page - 1) * records_per_page
