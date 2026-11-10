
import sqlite3
from pathlib import Path


# Get the database file location
DB_PATH = Path(__file__).resolve().parent / "monitoring.db"


def get_connection():

    connection = sqlite3.connect(DB_PATH)

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    # Create servers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servers (
            server_id TEXT PRIMARY KEY,
            server_name TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create health records table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            server_id TEXT NOT NULL,
            cpu_usage REAL,
            ram_usage REAL,
            disk_usage REAL,
            health_status TEXT NOT NULL,
            checked_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (server_id)
            REFERENCES servers(server_id)
        )
    """)

    # Create alerts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
            server_id TEXT NOT NULL,
            severity TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (server_id)
            REFERENCES servers(server_id)
        )
    """)

    connection.commit()

    connection.close()

    print("Database initialized successfully!")


if __name__ == "__main__":

    initialize_database()
