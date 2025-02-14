import os.path
from configparser import ConfigParser

PATH = 'config.ini'
class Config:
    def __init__(self, section):
        self.parser = ConfigParser()
        self.filename = PATH
        self.section = section

    def load(self):
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

    def is_configured(self):
        return os.path.isfile('./{}'.format(self.filename))

    def save(self, db_settings):
        self.parser.add_section(self.section)
        for key in db_settings:
            self.parser.set(self.section, key, db_settings[key])

        with open(self.filename, 'w') as configfile:
            self.parser.write(configfile)
            configfile.close()

    def update_value(self, key, new_value):
        self.parser.read(self.filename)
        postgres_section = self.parser[self.section]
        postgres_section[key] = new_value
        with open(self.filename, 'w') as configfile:
            self.parser.write(configfile)
            configfile.close()
