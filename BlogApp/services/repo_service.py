from injector import inject
from repository.posts_repo import PostsRepo

class RepoService:
    @inject
    def __init__(self, repo: PostsRepo):
        print(f"Repo instance is {repo}")
        self.repo = repo

    def get_repo(self):
        return self.repo
