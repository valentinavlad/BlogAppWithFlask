from setup.config import Config
from models.db_credentials import DbCredentials

class DatabaseConfig(Config):
    
    def __init__(self):
        super().__init__('postgresql')
        self.configured = self.is_configured()

    def load_configuration(self):
        super().load()

    def save_configuration(self, db_credentials: DbCredentials):
        db_settings = db_credentials.to_dictionary()
        super().save(db_settings)