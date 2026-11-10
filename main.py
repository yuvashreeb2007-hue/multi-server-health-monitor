
import logging
from pathlib import Path

from monitoring.server_simulator import simulate_servers
from monitoring.health_checker import display_health_report
from monitoring.alert_manager import generate_alerts, display_alerts

from database.save_servers import save_servers
from database.save_health import save_health_records
from database.save_alerts import save_alerts
from reports.export_reports import generate_reports


# Configure application logging
LOG_FILE = Path(__file__).resolve().parent / "logs" / "monitor.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def main():
    logging.info("Monitoring cycle started")

    print("\n===================================")
    print(" MULTI-SERVER HEALTH MONITORING")
    print("===================================\n")

    servers = simulate_servers()

    save_servers()
    display_health_report(servers)
    save_health_records()

    alerts = generate_alerts(servers)
    display_alerts(alerts)
    save_alerts()

    print("\nGenerating monitoring reports...")
    generate_reports()

    print("\nMonitoring cycle completed successfully!")

    logging.info("Monitoring cycle completed successfully")


if __name__ == "__main__":
    try:
        main()

    except Exception:
        logging.exception("Monitoring cycle failed")
        raise
