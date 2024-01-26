from dotenv import dotenv_values


class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config = dotenv_values(self.filepath)
    def database(self):
        db_config = {
          "database":self.config["DB_NAME"],
          "user":self.config["DB_USER"],
          "password":self.config["DB_PASS"],
          "host":self.config["DB_HOST"]
          }
        return db_config


