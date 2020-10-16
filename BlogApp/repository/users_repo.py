import abc

class UsersRepo(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is UsersRepo:
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
            if any("__check_user_exists__" in Q.__dict__
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
    def edit(cls, user):
        pass
    @abc.abstractclassmethod
    def delete(cls, pid):
        pass
    @abc.abstractclassmethod
    def add(cls, user):
        pass   
    @abc.abstractclassmethod
    def check_user_exists(cls, email):
        pass
