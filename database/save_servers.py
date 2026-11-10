
from database.db_manager import get_connection
from monitoring.server_simulator import simulate_servers


def save_servers():
    servers = simulate_servers()
    connection = get_connection()
    cursor = connection.cursor()

    for server in servers:
        cursor.execute(
            """
            INSERT OR REPLACE INTO servers
            (server_id, server_name, ip_address)
            VALUES (?, ?, ?)
            """,
            (
                server["ip"],
                server["name"],
                server["ip"]
            )
        )

    connection.commit()
    connection.close()

    print("Server information saved successfully!")


if __name__ == "__main__":
    save_servers()
