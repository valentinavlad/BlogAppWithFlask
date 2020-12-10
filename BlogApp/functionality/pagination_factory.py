from functionality.pagination import Pagination
from services.user_statistic import UserStatistic
from repository.posts_repo import PostsRepo

class PaginationFactory:
    @staticmethod
    def create_pagination(type):
        if type == 'UserStatistic':
            return Pagination()