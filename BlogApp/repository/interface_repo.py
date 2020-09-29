import abc
class InterfaceRepo(abc.ABC):
    """description of class"""
    @abc.abstractclassmethod
    def find_post_id(cls,pid):
        pass
    @abc.abstractclassmethod
    def view_posts(cls):
        pass
    @abc.abstractclassmethod
    def edit(cls, pid):
        pass
    @abc.abstractclassmethod
    def delete(cls, found_post, pid):
        pass
    @abc.abstractclassmethod
    def add(cls):
        pass

