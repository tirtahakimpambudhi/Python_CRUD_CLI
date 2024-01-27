# Assuming your Database class has a connection method, and Config class has a database method.
# Modify the imports if necessary.

import mysql.connector
from pydantic import ValidationError
import conf.config as config
import database.database as db
import model.contacts as model
import validation.contacts_validation as validation
import os

class Contact_Service():
    def __init__(self):
        try:
            self.config_instance = config.Config(os.path.join(os.getcwd(), ".env"))
            db_config = self.config_instance.database()
            self.db_instance = db.Database(db_config=db_config)
            self.model = model.Contacts(config=self.config_instance)
            self.validation = validation

            # setup
            self.db_instance.connect()  # Assuming this method exists in your Database class
            self.model.create_table()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_contact(self, contact):
        try:
            self.validation.ContactValidation(**contact)
            self.model.create_contact(contact=contact)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        except ValidationError as err_validation:
            print(err_validation)

    def update_contact(self,contact_id, contact):
        try:
            self.validation.ContactValidation(**contact)
            self.model.update_contact(contact_id=contact_id,contact=contact)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        except ValidationError as err_validation:
            print(err_validation)

    def delete_contact(self, contact_id):
        try:
            self.model.delete_contact(contact_id=contact_id)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def get_all_contacts(self):
        try:
            return self.model.get_all_contacts()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    def get_contact_by_id(self,contact_id):
        try:
            return self.model.get_by_id_contact(contact_id=contact_id)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None