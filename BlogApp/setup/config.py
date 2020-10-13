import os.path
from configparser import ConfigParser

class Config():
  
    def __init__(self):
        self.parser = ConfigParser()
        self.filename = 'database.ini'
        self.section = 'postgresql'
        self.configured = self.is_configured()

    def is_configured(self):
       return os.path.isfile('./{}'.format(self.filename))

    def save(self):
        self.parser.read(self.filename)
        db_settings = {}
        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            for param in params:
                db_settings[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'
                            .format(self.section, self.filename))
        return db_settings

    def load(self, database, user, password):
        self.parser.add_section(self.section)
        self.parser['postgresql']['host'] = 'localhost'
        self.parser['postgresql']['database'] = database
        self.parser['postgresql']['user'] = user
        self.parser['postgresql']['password'] = password
        self.parser['postgresql']['port'] = '5432'

        with open('database.ini', 'w') as configfile:
            self.parser.write(configfile)
            configfile.close()
