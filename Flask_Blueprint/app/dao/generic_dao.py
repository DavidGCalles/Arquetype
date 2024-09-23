"""This DAO represents the minimum entity to be used as DAO. Can be used as base class or totally rewritten."""

from app.services.db import get_db_connection

class BaseDAO:
    """
    Base Data Access Object class for handling database operations.

    Attributes:
        table (str): The name of the database table this DAO is associated with.
        connection: The database connection object.
    """
    def __init__(self):
        """
        Initializes the BaseDAO with a specific table name and database connection.
        """
        self.table = "users"
        self.connection = get_db_connection()

    def generic_get_all(self):
        """
        Fetches all records from the database table.

        Returns:
            list: A list of tuples representing each record fetched from the table.
        """
        query = f"SELECT * FROM {self.table}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def generic_insert(self, insert_data:dict):
        """
        Inserts a new record into the database table.

        Args:
            insert_data (dict): A dictionary containing column-value pairs to be inserted.

        Returns:
            int: The auto-generated ID of the newly inserted record.
        """
            # Extract keys and values from insert_data
        keys = ", ".join(insert_data.keys())
        placeholders = ", ".join(["%s"] * len(insert_data))  # Use placeholders for security

        # Construct the SQL query with placeholders
        query = f"INSERT INTO {self.table} ({keys}) VALUES ({placeholders});"

        # Convert insert_data values to a tuple for the execute method
        values = tuple(insert_data.values())

        # Create cursor, execute the query, and commit the changes
        cursor = self.connection.cursor()
        cursor.execute(query, values)  # Execute with values tuple to safely pass data
        new_id = cursor.lastrowid  # Retrieves the last inserted ID
        self.connection.commit()
        cursor.close()  # It's a good practice to close the cursor

        return new_id  # Return the autogenerated ID

    def generic_update(self, pk:str, update_data:dict):
        """
        Update a record in the database with new data provided in the update_data dictionary.

        This method dynamically constructs and executes an SQL UPDATE statement to modify a record
        in the database. It identifies the record to update using the primary key provided and updates
        the specified fields with new values.

        Parameters:
        - pk (str): The key in the update_data dictionary that holds the primary key of the record.
        - update_data (dict): A dictionary containing the fields to update with their new values. 
                            The dictionary must contain the primary key as one of its keys.

        Returns:
        - int: The number of rows affected by the update operation.

        Raises:
        - KeyError: If the primary key is not found in the update_data dictionary.
        - psycopg2.DatabaseError: If an error occurs during database operation."""
        primary_key = update_data.pop(pk)
        keys = ", ".join([f"{key} = %s" for key in update_data.keys()])
        values = list(update_data.values())
        values.append(primary_key)  # Append the primary key to values to use in the WHERE clause
        sql = f"UPDATE {self.table} SET {keys} WHERE {pk} = %s"

        # Execute the SQL command
        with self.connection.cursor() as cursor:
            cursor.execute(sql, values)
            self.connection.commit()  # Commit the changes

        return cursor.rowcount  # Return the number of rows affected
