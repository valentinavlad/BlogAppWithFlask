from repository.users_repo import UsersRepo

class DbUsersRepoSqlalchemy(UsersRepo):

    def find_by_id(self, pid):
        pass
    def check_user_exists(self, email):
        pass

    def check_user_exists_by_name(self, name):
        pass

    def edit(self, user):
        pass

    def delete(self, pid):
        pass

    def add(self, user):
        pass

    def view_all(self):
        pass
