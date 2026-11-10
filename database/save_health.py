
from database.db_manager import get_connection
from monitoring.server_simulator import simulate_servers
from monitoring.health_checker import check_server_health


def save_health_records():
    servers = simulate_servers()
    connection = get_connection()
    cursor = connection.cursor()

    for server in servers:
        health_status = check_server_health(server)

        cursor.execute(
            """
            INSERT INTO health_records
            (server_id, cpu_usage, ram_usage, disk_usage, health_status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                server["ip"],
                server["cpu"],
                server["ram"],
                server["disk"],
                health_status
            )
        )

    connection.commit()
    connection.close()

    print("Server health records saved successfully!")


if __name__ == "__main__":
    save_health_records()
