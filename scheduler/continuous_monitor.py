
import time
from datetime import datetime

from monitoring.server_simulator import simulate_servers
from monitoring.health_checker import display_health_report
from monitoring.alert_manager import generate_alerts, display_alerts

from database.save_servers import save_servers
from database.save_health import save_health_records
from database.save_alerts import save_alerts


INTERVAL = 30


def run_monitoring_cycle():
    print("\n" + "=" * 50)
    print("MONITORING CYCLE:", datetime.now())
    print("=" * 50)

    servers = simulate_servers()

    save_servers()
    display_health_report(servers)

    save_health_records()

    alerts = generate_alerts(servers)
    display_alerts(alerts)

    save_alerts()

    print("\nMonitoring cycle completed!")


def start_monitoring():
    print("CONTINUOUS SERVER MONITORING STARTED")
    print("Monitoring interval: 30 seconds")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            run_monitoring_cycle()
            print(f"\nNext check in {INTERVAL} seconds...")
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    start_monitoring()
