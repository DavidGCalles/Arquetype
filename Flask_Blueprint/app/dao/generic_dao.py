from app.services.db import get_db_connection

class BaseDAO:
    def __init__(self):
        self.table = "users"
        self.connection = get_db_connection()

    def generic_get_all(self):
        query = f"SELECT * FROM {self.table}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return data
        
    def generic_insert(self, insert_data:dict):
        keys = insert_data.keys()
        values = insert_data.values()
        query = f"INSERT INTO {self.table} ({','.join(keys)}) VALUES ({','.join(values)});"
        cursor = self.connection.cursor()
        cursor.execute(query)
        new_id = cursor.lastrowid  # Retrieves the last inserted ID
        self.connection.commit()
        cursor.close()
        self.connection.close()
        return new_id  # Return the autogenerated ID