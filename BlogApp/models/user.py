import datetime

class User:
    count = 1
    date_now = datetime.datetime.now()
    def __init__(self, name, email, password):
        self.user_id = User.count
        self.name = name
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        User.count += 1

    @classmethod
    def get_user(cls, row):
        cls.user_id = row[0]
        cls.name = row[1]
        cls.email = row[2]
        cls.password = row[3]
        cls.created_at = row[4]
        cls.modified_at = row[5]
        obj = cls(cls.name, cls.email, cls.password)
        obj.created_at = cls.created_at
        obj.modified_at = cls.modified_at
        obj.user_id = cls.user_id
        return obj
    
    
    @classmethod
    def unmapp_user(cls, user_repo):
        cls.user_id = user_repo.user_id
        cls.name = user_repo.name
        cls.email = user_repo.email
        cls.password = user_repo.password
        cls.created_at = user_repo.created_at
        cls.modified_at =  user_repo.modified_at
        return cls

    @staticmethod
    def get_list_from_result(result):
        list_dict = []
        for i in result:
            list_dict.append(i)
        return list_dict

    def __str__(self):
        return self.name + " " + self.email

    __repr__ = __str__
