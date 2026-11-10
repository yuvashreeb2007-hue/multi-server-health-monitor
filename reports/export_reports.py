
import csv
from pathlib import Path
from datetime import datetime

from database.db_manager import get_connection

REPORT_DIR = Path(__file__).resolve().parent


def export_health_csv():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            servers.server_name,
            servers.server_id,
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

    file_path = REPORT_DIR / "health_report.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Server Name",
            "IP Address",
            "CPU Usage",
            "RAM Usage",
            "Disk Usage",
            "Health Status",
            "Checked At"
        ])

        writer.writerows(records)

    print(f"CSV report created: {file_path}")


def export_text_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM servers")
    total_servers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM health_records")
    total_records = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts")
    total_alerts = cursor.fetchone()[0]

    cursor.execute("""
        SELECT server_name, server_id
        FROM servers
    """)
    servers = cursor.fetchall()

    cursor.execute("""
        SELECT
            servers.server_name,
            alerts.severity,
            alerts.message,
            alerts.created_at
        FROM alerts
        JOIN servers
        ON alerts.server_id = servers.server_id
        ORDER BY alerts.alert_id DESC
    """)
    alerts = cursor.fetchall()

    connection.close()

    file_path = REPORT_DIR / "monitoring_report.txt"

    with open(file_path, "w") as file:
        file.write("MULTI-SERVER MONITORING REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write("DATABASE SUMMARY\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total Servers: {total_servers}\n")
        file.write(f"Health Records: {total_records}\n")
        file.write(f"Total Alerts: {total_alerts}\n\n")

        file.write("REGISTERED SERVERS\n")
        file.write("-" * 40 + "\n")

        for name, ip in servers:
            file.write(f"{name} - {ip}\n")

        file.write("\nALERT HISTORY\n")
        file.write("-" * 40 + "\n")

        for name, severity, message, created_at in alerts:
            file.write(
                f"{name} | {severity} | {message} | {created_at}\n"
            )

    print(f"Text report created: {file_path}")


def generate_reports():
    export_health_csv()
    export_text_report()


if __name__ == "__main__":
    generate_reports()
