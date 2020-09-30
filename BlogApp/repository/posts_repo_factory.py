from repository.in_memory_posts import InMemoryPosts
from repository.database_posts_repo import DatabasePostRepo

class PostsRepoFactory():

    @staticmethod
    def get_repo(type):
        try:
            if type == "InMemoryPosts":
                return InMemoryPosts()
            if type == "DatabasePostRepo":
                return DatabasePostRepo()
            raise AssertionError("Repo not found")
        except AssertionError as _e:
            print(_e)