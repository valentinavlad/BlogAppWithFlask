from repository.in_memory_db import InMemoryDb
from repository.repo_db import RepoDb

class RepoFactory():

    @staticmethod
    def get_repo(type):
        try:
            if type == "InMemoryDb":
                return InMemoryDb()
            if type == "RepoDb":
                return RepoDb()
            raise AssertionError("Repo not found")
        except AssertionError as _e:
            print(_e)
