class LoginValidator:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_form(self):
        error = None
        if not self.email:
            error = 'Email is required.'
        elif not self.password:
            error = 'Password is required.'
        return error

    @staticmethod
    def check_user(user):
        if user is None:
            error = 'User {} is not registered.'.format(user.name)
        return error
