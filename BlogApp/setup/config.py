from configparser import ConfigParser

class Config:
    def __init__(self):
        # create a parser
        self.parser = ConfigParser()
        self.filename = 'database.ini'
        self.section = 'postgresql'

    def config(self):
        # read config file
        self.parser.read(self.filename)
        # get section, default to postgresql
        db_posts = {}
        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            for param in params:
                db_posts[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'
                            .format(self.section, self.filename))
        return db_posts

    def write_config_data(self, database, user, password):
        self.parser.add_section(self.section)
        self.parser['postgresql']['host'] = 'localhost'
        self.parser['postgresql']['database'] = database
        self.parser['postgresql']['user'] = user
        self.parser['postgresql']['password'] = password
        self.parser['postgresql']['port'] = '5432'

        with open('database.ini', 'w') as configfile:
            self.parser.write(configfile)
