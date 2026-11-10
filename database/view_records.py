
from database.db_manager import get_connection
from rich.console import Console
from rich.table import Table

console = Console()


def show_database_summary():
    connection = get_connection()
    cursor = connection.cursor()

    queries = [
        ("Total Servers", "SELECT COUNT(*) FROM servers"),
        ("Health Records", "SELECT COUNT(*) FROM health_records"),
        ("Total Alerts", "SELECT COUNT(*) FROM alerts")
    ]

    table = Table(title="DATABASE SUMMARY")
    table.add_column("Information")
    table.add_column("Count", justify="center")

    for label, query in queries:
        cursor.execute(query)
        count = cursor.fetchone()[0]
        table.add_row(label, str(count))

    console.print(table)

    cursor.execute("""
        SELECT server_name, server_id
        FROM servers
    """)

    server_table = Table(title="REGISTERED SERVERS")
    server_table.add_column("Server Name")
    server_table.add_column("IP Address")

    for name, ip in cursor.fetchall():
        server_table.add_row(name, ip)

    console.print(server_table)

    connection.close()


if __name__ == "__main__":
    show_database_summary()
