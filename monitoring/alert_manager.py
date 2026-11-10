
from rich.console import Console
from rich.table import Table

from monitoring.server_simulator import simulate_servers
from monitoring.health_checker import check_server_health

console = Console()


def generate_alerts(servers):

    alerts = []

    for server in servers:

        health = check_server_health(server)

        if health == "OFFLINE":

            alerts.append({
                "server": server["name"],
                "severity": "CRITICAL",
                "message": "Server is offline or unavailable"
            })

            continue

        metrics = {
            "CPU": server["cpu"],
            "RAM": server["ram"],
            "Disk": server["disk"]
        }

        for metric, value in metrics.items():

            if value >= 90:

                alerts.append({
                    "server": server["name"],
                    "severity": "CRITICAL",
                    "message": f"{metric} usage is critically high: {value}%"
                })

            elif value >= 80:

                alerts.append({
                    "server": server["name"],
                    "severity": "WARNING",
                    "message": f"{metric} usage is high: {value}%"
                })

    return alerts


def display_alerts(alerts):

    table = Table(title="Server Alert Management System")

    table.add_column("Server")
    table.add_column("Severity")
    table.add_column("Alert Message")

    if not alerts:

        console.print("[green]No alerts! All servers are healthy.[/green]")
        return

    for alert in alerts:

        severity = alert["severity"]

        if severity == "CRITICAL":
            color = "bold red"
        else:
            color = "yellow"

        table.add_row(
            alert["server"],
            f"[{color}]{severity}[/{color}]",
            alert["message"]
        )

    console.print(table)


if __name__ == "__main__":

    servers = simulate_servers()

    alerts = generate_alerts(servers)

    display_alerts(alerts)
