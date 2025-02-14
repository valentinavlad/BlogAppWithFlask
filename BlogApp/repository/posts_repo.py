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
            if any("__get_all__" in Q.__dict__
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
    def edit(cls, post):
        pass
    @abc.abstractclassmethod
    def delete(cls, pid):
        pass
    @abc.abstractclassmethod
    def add(cls, post):
        pass
    @abc.abstractclassmethod
    def get_all(cls, owner_id, records_per_page, offset):
        pass
    @abc.abstractclassmethod
    def get_count(cls, owner_id):
        pass
