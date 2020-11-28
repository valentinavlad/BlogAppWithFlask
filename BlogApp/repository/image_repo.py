import abc
import os

FILE_EXTENSIONS = ['.jpg', '.png', '.gif', '.jpeg', '.eps', '.bmp', '.tif', '.tiff']

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
    def edit(cls, filename, file_storage):
        pass
    @abc.abstractclassmethod
    def delete(cls, filename):
        pass
    @abc.abstractclassmethod
    def add(cls, file_storage):
        pass
    @abc.abstractclassmethod
    def get(cls, filename):
        pass
    @staticmethod
    def check_img_extension(filename):
        file_ext = os.path.splitext(filename)[1]
        if file_ext.lower() not in FILE_EXTENSIONS:
            return False
        return True
