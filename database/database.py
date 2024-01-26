import mysql.connector

class Database:
  def __init__ (self,db_config):
    self.db_config = db_config
    self.connection = None
    self.cursor = None
  
  def connect(self):
    try:
      self.connection = mysql.connector.connect(**self.db_config)
      self.cursor = self.connection.cursor()
    except mysql.connector.Error as err:
      print(f"Error : {err}")
  def execute(self,query,data=None):
    try:
      self.cursor.execute(query,data)
    except mysql.connector.Error as err:
      print(f"Error Execute: {err}")
  
  def query(self,query,data=None):
    try:
      self.cursor.execute(query,data)
      return self.cursor.fetchall()
    except mysql.connector.Error as err:
      print(f"Error Execute: {err}")
      return None
  def commit(self):
    try:
      self.connection.commit()
      print("Changes committed to the database")
    except mysql.connector.Error as err:
      print(f"Error committing changes: {err}")
  def close(self):
    if self.connection.is_connected():
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

    