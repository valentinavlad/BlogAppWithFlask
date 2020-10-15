from setup.config import Config
from models.db_credentials import DbCredentials

class DatabaseConfig(Config):
    def __init__(self):
        super().__init__('postgresql')

    def load_configuration(self):
        db_settings = super().load()
        db_credentials = \
            DbCredentials(db_settings['user'], db_settings['database'], db_settings['password'])
        return db_credentials

    def save_configuration(self, db_credentials: DbCredentials):
        db_settings = db_credentials.to_dictionary()
        super().save(db_settings)
