from repository.posts_repo_factory import PostsRepoFactory

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    PostsRepoFactory.get_repo("DatabasePostRepo")

class DevelopmentConfig(Config):
    DEBUG = True
    PostsRepoFactory.get_repo("DatabasePostRepo")
class TestingConfig(Config):
    TESTING = True
    PostsRepoFactory.get_repo("InMemoryPosts")