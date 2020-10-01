from repository.in_memory_posts import InMemoryPosts
from repository.database_posts_repo import DatabasePostRepo

class PostsRepoFactory():

    @staticmethod
    def get_repo(repo_type):
        if repo_type == "InMemoryPosts":
            return InMemoryPosts()
        if repo_type == "DatabasePostRepo":
            return DatabasePostRepo()
        raise AssertionError("Repo not found")
