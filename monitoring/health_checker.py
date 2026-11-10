
from rich.console import Console
from rich.table import Table

from monitoring.server_simulator import simulate_servers

console = Console()


def check_server_health(server):

    if server["status"] == "OFFLINE":
        return "OFFLINE"

    cpu = server["cpu"]
    ram = server["ram"]
    disk = server["disk"]

    metrics = [cpu, ram, disk]

    if any(value >= 90 for value in metrics):
        return "CRITICAL"

    if any(value >= 80 for value in metrics):
        return "WARNING"

    return "HEALTHY"


def display_health_report(servers):

    table = Table(title="Server Health Status Report")

    table.add_column("Server")
    table.add_column("CPU")
    table.add_column("RAM")
    table.add_column("Disk")
    table.add_column("Health Status")

    for server in servers:

        health = check_server_health(server)

        if health == "HEALTHY":
            color = "green"

        elif health == "WARNING":
            color = "yellow"

        elif health == "CRITICAL":
            color = "bold red"

        else:
            color = "dim red"

        cpu = f'{server["cpu"]}%' if server["cpu"] is not None else "--"
        ram = f'{server["ram"]}%' if server["ram"] is not None else "--"
        disk = f'{server["disk"]}%' if server["disk"] is not None else "--"

        table.add_row(
            server["name"],
            cpu,
            ram,
            disk,
            f"[{color}]{health}[/{color}]"
        )

    console.print(table)


if __name__ == "__main__":

    servers = simulate_servers()

    display_health_report(servers)
