from repository.users_data import dummy_users
from repository.posts_data import dummy_posts
from repository.database_users_repo import UsersRepo

class InMemoryUsersRepo(UsersRepo):
    def __init__(self):
        pass
    def find_by_id(self, pid):
        found_user = None
        for user in dummy_users:
            if user.user_id == pid:
                found_user = user
        return found_user

    def view_all(self):
        return dummy_users

    def edit(self, user):
        index = dummy_users.index(user)
        dummy_users[index] = user

    def delete(self, pid):
        user = self.find_by_id(pid)
        for post in dummy_posts:
            if int(post.owner) == pid:
                dummy_posts.remove(post)

        dummy_users.remove(user)

    def add(self, user):
        dummy_users.insert(0, user)

    def check_user_exists(self, email):
        found_user = None
        for user in dummy_users:
            if user.email == email:
                found_user = user
        return found_user
    def check_user_exists_by_name(self, name):
        found_user = None
        for user in dummy_users:
            if user.name == name:
                found_user = user
        return found_user
