import abc

class ConfigInterface(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is ConfigInterface:
            if any("__save__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__load__" in Q.__dict__
                   for Q in C.__mro__):
                return True
            if any("__is_configured__" in Q.__dict__
                   for Q in C.__mro__):
                return True
        return False

    @abc.abstractclassmethod
    def save(cls):
        pass

    @abc.abstractclassmethod
    def load(cls, database, user, password):
        pass

    @abc.abstractclassmethod
    def is_configured(cls):
        pass

