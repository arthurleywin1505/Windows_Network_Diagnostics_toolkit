import json
from pathlib import Path
from modules.connectivity import check_ping
from modules.dns_checker import check_dns
from modules.latency_monitor import measure_latency
from modules.ip_analyzer import get_ip_config
from modules.route_analyzer import get_routes
from modules.connection_monitor import get_connections

ROOT = Path(__file__).parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
REPORT_DIR = ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

def run_all():
    results = {}
    results["Internet (1.1.1.1)"] = check_ping(CONFIG["internet_test_host"], CONFIG["ping_count"], CONFIG["timeout_ms"])
    results["Gateway"] = check_ping(get_ip_config().get("gateway") or "", CONFIG["ping_count"], CONFIG["timeout_ms"])
    results["DNS"] = check_dns(CONFIG["dns_test_host"])
    results["Latency"] = measure_latency(CONFIG["latency_target"], CONFIG["ping_count"], CONFIG["timeout_ms"])
    results["IP Configuration"] = get_ip_config()
    results["Routes"] = get_routes()
    results["Active Connections"] = get_connections()
    return results

def display(title, value):
    print(f"\n--- {title} ---")
    if isinstance(value, dict):
        for k, v in value.items():
            print(f"{k}: {v}")
    elif isinstance(value, list):
        for item in value[:30]:
            print(item)
        if len(value) > 30:
            print(f"... and {len(value)-30} more entries")
    else:
        print(value)

def save_report(results):
    from datetime import datetime
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = REPORT_DIR / f"diagnostic_report_{stamp}.txt"
    lines = ["WINDOWS NETWORK DIAGNOSTICS REPORT", "=" * 38, f"Generated: {datetime.now()}", ""]
    for title, value in results.items():
        lines += [f"[{title}]", str(value), ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport saved: {path}")

def main():
    latest = {}
    while True:
        print("""
========================================
 WINDOWS NETWORK DIAGNOSTICS TOOLKIT
========================================
1. Check Internet Connectivity
2. Check Default Gateway
3. DNS Resolution Test
4. Latency Monitoring
5. View IP Configuration
6. View Routing Table
7. View Active Connections
8. Run Complete Diagnostics
9. Save Last Results as Report
0. Exit
""")
        choice = input("Select an option: ").strip()
        if choice == "1":
            latest["Internet"] = check_ping(CONFIG["internet_test_host"], CONFIG["ping_count"], CONFIG["timeout_ms"])
            display("Internet Connectivity", latest["Internet"])
        elif choice == "2":
            gateway = get_ip_config().get("gateway")
            latest["Gateway"] = check_ping(gateway or "", CONFIG["ping_count"], CONFIG["timeout_ms"])
            display("Gateway", latest["Gateway"])
        elif choice == "3":
            latest["DNS"] = check_dns(CONFIG["dns_test_host"])
            display("DNS Test", latest["DNS"])
        elif choice == "4":
            latest["Latency"] = measure_latency(CONFIG["latency_target"], CONFIG["ping_count"], CONFIG["timeout_ms"])
            display("Latency", latest["Latency"])
        elif choice == "5":
            latest["IP Configuration"] = get_ip_config()
            display("IP Configuration", latest["IP Configuration"])
        elif choice == "6":
            latest["Routes"] = get_routes()
            display("Routing Table", latest["Routes"])
        elif choice == "7":
            latest["Active Connections"] = get_connections()
            display("Active Connections", latest["Active Connections"])
        elif choice == "8":
            latest = run_all()
            for title, value in latest.items():
                display(title, value)
            save_report(latest)
        elif choice == "9":
            if latest:
                save_report(latest)
            else:
                print("No results yet. Run a diagnostic option first.")
        elif choice == "0":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid option. Enter 0-9.")

if __name__ == "__main__":
    main()
