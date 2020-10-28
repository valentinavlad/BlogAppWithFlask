from setup.config import Config
from models.db_info import DbInfo

class DbInfoConfig(Config):
    def __init__(self):
        super().__init__('info')

    def load_configuration(self):
        db_settings = super().load()
        db_credentials = DbInfo()
        return db_credentials

    def save_configuration(self, db_credentials: DbInfo):
        db_settings = db_credentials.to_dictionary()
        super().save(db_settings)

