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
            print ("DB POSTS FROM CONFIG FUNCTION,", db_posts.keys)
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db_posts
    # save configuration
    def write_config_data(self, user, password, database):
        self.parser.add_section('postgresql')
        self.parser['postgresql']['host'] = 'localhost'
        self.parser['postgresql']['database'] = database
        self.parser['postgresql']['user'] = user
        self.parser['postgresql']['password'] = password
      
        with open('database.ini', 'w') as configfile:
            config.write(configfile)

    # load configuration
    def read_config_data(self, filename):
        self.parser.read(filename)
        for section in self.parser.sections():
            print('Section: ', section)
            for k, v in self.parser.items(section):
                print(' {} = {}'.format(k, v))
            print()

    def read_data(self, file):
        # read and parse the configuration file.
        self.parser.read(file)
        # get option value in specified section.
        user = self.parser.get('postgresql', 'host')
        database = self.parser.get('postgresql', 'database')
        print('database is ', database)
        user = self.parser.get('postgresql', 'user')
        password = self.parser.get('postgresql', 'password')

    def write_data(self, user, password, database):
        self.parser.add_section('postgresql')
        self.parser.set('postgresql', 'host', database, user, password)
        # open a configuration file
        file = open('database1.ini')
        # write the new section and options to the file.
        self.parser.write(file)
        file.close()

    def load_config(self, file, config={}):
        """
        returns a dictionary with keys of the form
        <section>.<option> and the corresponding values
        """
        config = config.copy(  )
        self.parser.read(file)
        for sec in self.parser.sections():
            name = string.lower(sec)
            for opt in cp.options(sec):
                config[name + "." + string.lower(opt)] = string.strip(
                    self.parser.get(sec, opt))
        return config

    def get_connection_by_config(self, config_file_path, section_name):
        if(len(config_file_path) > 0 and len(section_name) > 0):
            # read the configuration file.
            self.parser.read(config_file_path)
            # if the configuration file contains the provided section name.
            if(self.parser.has_section(section_name)):
                # read the options of the section. the config_params is a list object.
                config_params = self.parser.items(section_name)
                # so we need below code to convert the list object to a python dictionary object.
                # define an empty dictionary.
                db_conn_dict = {}
                # loop in the list.
                for config_param in config_params:
                    # get options key and value.
                    key = config_param[0]
                    value = config_param[1]
                    # add the key value pair in the dictionary object.
                    db_conn_dict[key] = value
                # get connection object use above dictionary object.
                conn = psycopg2.connect(**db_conn_dict)

                #nu am variabila membra _conn!!!!
                self._conn = conn
                print("******* get postgresql database connection with configuration file ********", "\n")