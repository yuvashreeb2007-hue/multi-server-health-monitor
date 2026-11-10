
# Multi-Server Health Monitoring and Automated Status Reporting System

## 1. Project Overview

This project is a Python-based Linux server monitoring application.

It monitors simulated servers, identifies health conditions, generates alerts, stores monitoring history in an SQLite database, and automatically exports health reports.

The application uses a Rich terminal interface and systemd for scheduled execution.

## 2. Features

- Simulated multi-server monitoring
- CPU, RAM, and disk usage tracking
- HEALTHY, WARNING, CRITICAL, and OFFLINE status detection
- Automatic alert generation
- SQLite database integration
- Health history tracking
- CSV and text report generation
- Continuous monitoring
- systemd timer automation
- Application logging and error handling

## 3. Technologies Used

- Python
- SQLite
- Rich
- psutil
- Linux systemd
- CSV

## 4. Project Structure

```text
multi-server-monitor/
├── config/
├── monitoring/
│   ├── server_simulator.py
│   ├── health_checker.py
│   └── alert_manager.py
├── database/
│   ├── db_manager.py
│   ├── save_servers.py
│   ├── save_health.py
│   ├── save_alerts.py
│   ├── view_records.py
│   └── monitoring.db
├── reports/
│   ├── health_history.py
│   ├── export_reports.py
│   ├── health_report.csv
│   └── monitoring_report.txt
├── scheduler/
│   └── continuous_monitor.py
├── logs/
│   └── monitor.log
├── main.py
└── README.md
```

## 5. Installation

Clone the repository and enter the project directory.

```bash
git clone <your-repository-url>
cd multi-server-monitor
```

Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies.

```bash
pip install rich psutil
```

Initialize the database.

```bash
python -m database.db_manager
```

## 6. Run the Application

```bash
python main.py
```

## 7. View Database Records

```bash
python -m database.view_records
```

View health history:

```bash
python -m reports.health_history
```

Generate reports:

```bash
python -m reports.export_reports
```

## 8. Automated Monitoring

The application can run periodically using a systemd user timer.

Check timer status:

```bash
systemctl --user status multi-server-monitor.timer
```

Start the timer:

```bash
systemctl --user enable --now multi-server-monitor.timer
```

Stop the timer:

```bash
systemctl --user stop multi-server-monitor.timer
```

View service logs:

```bash
journalctl --user -u multi-server-monitor.service
```

## 9. Generated Reports

- `reports/health_report.csv` — detailed server health history.
- `reports/monitoring_report.txt` — monitoring summary and alert history.
- `logs/monitor.log` — application execution and error logs.

## 10. Current Monitoring Mode

The current version uses simulated server data for demonstration and testing.

The architecture can be extended to monitor real remote Linux servers through SSH.

## 11. Author

Developed as a Linux and Python system monitoring project.
