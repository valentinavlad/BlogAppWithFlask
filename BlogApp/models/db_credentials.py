class DbCredentials:
    def __init__(self, user, database, password):
        self.user = user
        self.password = password
        self.database = database
        self.port = '5432'
        self.host = 'localhost'

    def to_dictionary(self):
        db_settings = {}
        db_settings['host'] = self.host
        db_settings['database'] = self.database
        db_settings['user'] = self.user
        db_settings['password'] = self.password
        db_settings['port'] = self.port
        return db_settings
