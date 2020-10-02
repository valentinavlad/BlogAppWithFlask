from repository.in_memory_posts_repo import InMemoryPostsRepo
from repository.database_posts_repo import DatabasePostRepo

class PostsRepoFactory():
    testing = False
    @staticmethod
    def get():
        if PostsRepoFactory.testing:
            return InMemoryPostsRepo()
        if not PostsRepoFactory.testing:
            return DatabasePostRepo()
        raise AssertionError("Repo not found")
