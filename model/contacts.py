import mysql.connector
import database.database as DB

class Contacts(DB.Database):
    def __init__(self, config):
        self.config = config
        super().__init__(self.config.database())

    def create_table(self):
        with self:
            query = f"""
            CREATE TABLE IF NOT EXISTS {self.config.config['TB_NAME']} (
                id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                phone VARCHAR(20) NOT NULL,
                address VARCHAR(255) NOT NULL,
                category ENUM('FRIENDS', 'FAMILY', 'WORKER') NOT NULL
            );
            """
            self.execute(query)

    def get_all_contacts(self):
        try:
            with self:
                query = f"SELECT * FROM {self.config.config['TB_NAME']};"
                data = self.query(query)
                return data
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def get_by_id_contact(self, contact_id):
        try:
            with self:
                query = f"SELECT * FROM {self.config.config['TB_NAME']} WHERE id = %s;"
                data = self.query(query, data=(contact_id,))
                return data
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def create_contact(self, contact):
        try:
            with self:
                query = f"INSERT INTO {self.config.config['TB_NAME']} ({','.join(contact.keys())}) VALUES ({','.join(['%s'] * len(contact))})"
                self.execute(query, data=tuple(contact.values()))
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return err

    def update_contact(self, contact_id, updated_data):
        try:
            with self:
                query = f"UPDATE {self.config.config['TB_NAME']} SET {', '.join([f'{key} = %s' for key in updated_data.keys()])} WHERE id = %s"
                self.execute(query, data=tuple(list(updated_data.values()) + [contact_id]))
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return err

    def delete_contact(self, contact_id):
        try:
            with self:
                query = f"DELETE FROM {self.config.config['TB_NAME']} WHERE id = %s"
                self.execute(query, data=(contact_id,))
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return err
