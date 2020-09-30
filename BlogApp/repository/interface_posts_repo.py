import abc
from models.post import Post

class InterfacePostRepo(abc.ABC):
    """description of class"""
    @abc.abstractclassmethod
    def find_post_id(cls,pid):
        pass
    @abc.abstractclassmethod
    def view_posts(cls):
        pass
    @abc.abstractclassmethod
    def edit_post(cls, post):
        pass
    @abc.abstractclassmethod
    def delete_post(cls, pid):
        pass
    @abc.abstractclassmethod
    def add_post(cls, post):
        pass

