import psycopg2
import os #for enviroment variables.

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"), #use enviroment variables or set defaults.
            database=os.environ.get("DB_NAME", "clueless_db"),
            user=os.environ.get("DB_USER", "your_user"),
            password=os.environ.get("DB_PASSWORD", "your_password")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None