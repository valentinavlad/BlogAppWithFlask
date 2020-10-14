from setup.config import Config1

class DatabaseConfig(Config1):
   def __init__(self):
        super().__init__(self, 'postgresql')
   


