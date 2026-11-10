

from database.db_manager import get_connection
from monitoring.server_simulator import simulate_servers
from monitoring.alert_manager import generate_alerts


def save_alerts():
    servers = simulate_servers()
    alerts = generate_alerts(servers)

    # Create a mapping between server names and IP addresses
    server_ids = {
        server["name"]: server["ip"]
        for server in servers
    }

    connection = get_connection()
    cursor = connection.cursor()

    for alert in alerts:
        server_id = server_ids[alert["server"]]

        cursor.execute(
            """
            INSERT INTO alerts
            (server_id, severity, message)
            VALUES (?, ?, ?)
            """,
            (
                server_id,
                alert["severity"],
                alert["message"]
            )
        )

    connection.commit()
    connection.close()

    print(f"{len(alerts)} alerts saved successfully!")


if __name__ == "__main__":
    save_alerts()
