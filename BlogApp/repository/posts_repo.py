import abc

class PostsRepo(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is PostsRepo:
            if any("__add__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__delete__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__edit__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__view_all__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__find_by_id__" in Q.__dict__
                   for Q in C.__mro__):
                return True
        return False
    @abc.abstractclassmethod
    def find_by_id(cls, pid):
        pass
    @abc.abstractclassmethod
    def view_all(cls):
        pass
    @abc.abstractclassmethod
    def edit(cls, post):
        pass
    @abc.abstractclassmethod
    def delete(cls, pid):
        pass
    @abc.abstractclassmethod
    def add(cls, post):
        pass
