from setup.config import Config

class DatabaseConfig(Config):
   def __init__(self):
        super().__init__('postgresql')

   @staticmethod
   def create_dict(user, database, password):
       db_settings = {}
       db_settings['host'] = 'localhost'
       db_settings['database'] = database
       db_settings['user'] = user
       db_settings['password'] = password
       db_settings['port'] = '5432'
       return db_settings
