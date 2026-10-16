import os
import mysql.connector
from mysql.connector import Error

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "portfolio_db"),
}


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"[DB] Connection error: {e}")
        return None


def test_connection():
    connection = get_connection()
    if connection:
        print("[DB] Connected to XAMPP MySQL successfully.")
        connection.close()
        return True
    print(
        "[DB] Failed to connect. Start MySQL in XAMPP and verify that "
        f"the '{DB_CONFIG['database']}' database exists."
    )
    return False


if __name__ == "__main__":
    test_connection()
    