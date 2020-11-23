import abc

class ImageRepo(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is ImageRepo:
            if any("__add__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__delete__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__edit__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__get__" in Q.__dict__
                   for Q in C.__mro__):
                return True
        return False

    @abc.abstractclassmethod
    def edit(cls, post):
        pass
    @abc.abstractclassmethod
    def delete(cls, filename):
        pass
    @abc.abstractclassmethod
    def add(cls, post):
        pass
    @abc.abstractclassmethod
    def get(cls, owner_id, records_per_page, offset):
        pass
