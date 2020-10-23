from werkzeug.security import check_password_hash

class PasswordManager:
    @staticmethod
    def is_correct_password(password, user):
        return check_password_hash(user.password, password)
