import abc
from models.post import Post

class InterfacePostRepo(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C): 
        if cls is A: 
            if any("__add_post__" in Q.__dict__  
                    for Q in C.__mro__):  
                return True 
            if any("__delete_post__" in Q.__dict__  
                    for Q in C.__mro__):  
                return True 
            if any("__edit_post__" in Q.__dict__  
                    for Q in C.__mro__):  
                return True 
            if any("__view_posts__" in Q.__dict__  
                    for Q in C.__mro__):  
                return True 
            if any("__find_post_id__" in Q.__dict__  
                    for Q in C.__mro__):  
                return True 
        return False
  
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

