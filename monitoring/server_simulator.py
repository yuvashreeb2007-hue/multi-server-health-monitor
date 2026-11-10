
from rich.console import Console
from rich.table import Table


console = Console()


def simulate_servers():

    servers = [
        {
            "name": "Web Server",
            "ip": "192.168.1.101",
            "status": "ONLINE",
            "cpu": 28,
            "ram": 45,
            "disk": 52
        },
        {
            "name": "Database Server",
            "ip": "192.168.1.102",
            "status": "ONLINE",
            "cpu": 82,
            "ram": 68,
            "disk": 71
        },
        {
            "name": "File Server",
            "ip": "192.168.1.103",
            "status": "ONLINE",
            "cpu": 94,
            "ram": 91,
            "disk": 88
        },
        {
            "name": "Backup Server",
            "ip": "192.168.1.104",
            "status": "OFFLINE",
            "cpu": None,
            "ram": None,
            "disk": None
        }
    ]

    return servers


def display_servers(servers):

    table = Table(title="Multi-Server Health Monitoring")

    table.add_column("Server Name")
    table.add_column("IP Address")
    table.add_column("Status")
    table.add_column("CPU")
    table.add_column("RAM")
    table.add_column("Disk")

    for server in servers:

        status = server["status"]

        if status == "ONLINE":
            status = "[green]ONLINE[/green]"
        else:
            status = "[red]OFFLINE[/red]"

        cpu = f'{server["cpu"]}%' if server["cpu"] is not None else "--"
        ram = f'{server["ram"]}%' if server["ram"] is not None else "--"
        disk = f'{server["disk"]}%' if server["disk"] is not None else "--"

        table.add_row(
            server["name"],
            server["ip"],
            status,
            cpu,
            ram,
            disk
        )

    console.print(table)


if __name__ == "__main__":

    server_data = simulate_servers()

    display_servers(server_data)
