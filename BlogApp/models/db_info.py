class DbInfo:
    def __init__(self):
        self.version = '0'
    def to_dictionary(self):
        db_settings = {}
        db_settings['versio'] = self.version
        return db_settings
