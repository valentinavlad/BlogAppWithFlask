from configparser import ConfigParser

class Config:
    def __init__(self):
         # create a parser
        self.parser = ConfigParser()

    def config(self, filename='database.ini', section='postgresql'):
        # read config file
        self.parser.read(filename)

        # get section, default to postgresql
        db_posts = {}
        if self.parser.has_section(section):
            params = self.parser.items(section)
            for param in params:
                db_posts[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db_posts
    # save configuration
    def write_config_data(self, user, password, db):
        self.parser.add_section('postgresql')
        self.parser['postgresql']['host'] = 'localhost'
        self.parser['postgresql']['user'] = user
        self.parser['postgresql']['password'] = password
        self.parser['postgresql']['db'] = db

        with open('database.ini', 'w') as configfile:
            config.write(configfile)

    # load configuration