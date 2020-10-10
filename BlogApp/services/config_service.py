from injector import inject
from setup.config_interface import ConfigInterface

class ConfigService:
    @inject
    def __init__(self, config: ConfigInterface):
        print(f"Config instance is {config}")
        self.config = config
