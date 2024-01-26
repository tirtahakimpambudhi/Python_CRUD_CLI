import conf.config as config
import database.database as db
import os
def main():
  config_instance = config.Config(os.path.join(os.getcwd(),".env"))
  db_instance = db.Database(config_instance.database())
  print(config_instance.database())
  print(db_instance)
  
if __name__ == '__main__':
  main()