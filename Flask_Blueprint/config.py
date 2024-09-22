"""This module stores all config strings and details needed to run the app"""
class Config:
    """Stores every config detail needed"""
    SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key
    SWAGGER = {
        'title': 'Flask API',
        'uiversion': 3
    }
    DB_HOST = 'db'
    DB_PORT = '3306'
    DB_NAME = 'your_database_name'
    DB_USER = 'root'
    DB_PASSWORD = 'toor'
