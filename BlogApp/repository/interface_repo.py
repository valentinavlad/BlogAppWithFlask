import abc
class InterfaceRepo(abc.ABC):
    """description of class"""
    @abc.abstractclassmethod
    def find_post_id(self,pid):
        pass
    @abc.abstractclassmethod
    def view_posts(self):
        pass
    @abc.abstractclassmethod
    def edit(self, pid):
        pass
    @abc.abstractclassmethod
    def delete(self, found_post, pid):
        pass
    @abc.abstractclassmethod
    def add(self):
        pass

