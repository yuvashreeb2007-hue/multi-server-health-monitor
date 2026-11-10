
from database.db_manager import get_connection
from rich.console import Console
from rich.table import Table

console = Console()


def show_health_history():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            servers.server_name,
            health_records.cpu_usage,
            health_records.ram_usage,
            health_records.disk_usage,
            health_records.health_status,
            health_records.checked_at
        FROM health_records
        JOIN servers
        ON health_records.server_id = servers.server_id
        ORDER BY health_records.record_id DESC
    """)

    records = cursor.fetchall()
    connection.close()

    table = Table(title="SERVER HEALTH HISTORY")

    table.add_column("Server")
    table.add_column("CPU")
    table.add_column("RAM")
    table.add_column("Disk")
    table.add_column("Status")
    table.add_column("Checked At")

    for record in records:
        name, cpu, ram, disk, status, checked_at = record

        table.add_row(
            name,
            f"{cpu}%" if cpu is not None else "--",
            f"{ram}%" if ram is not None else "--",
            f"{disk}%" if disk is not None else "--",
            status,
            checked_at
        )

    console.print(table)


if __name__ == "__main__":
    show_health_history()
