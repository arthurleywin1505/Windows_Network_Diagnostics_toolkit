# Windows Network Diagnostics & Monitoring Toolkit

A Python + Windows CMD/PowerShell toolkit for collecting basic network diagnostics and identifying common connectivity problems.

## Features
- Internet reachability check
- Default gateway reachability check
- DNS lookup test
- Latency sampling
- IP configuration summary
- Routing table capture
- Active TCP connection summary
- Text diagnostic report generation

> **Important:** This is a local diagnostic utility. Results depend on your network and Windows configuration. The included sample report is illustrative and is not evidence of a live test.

## Requirements
- Windows 10/11
- Python 3.9+
- No third-party Python packages required

## Run
1. Extract the ZIP.
2. Open Command Prompt in the project folder.
3. Run:
   ```cmd
   python --version
   ```
4. Start the toolkit:
   ```cmd
   python main.py
   ```
   Or double-click `scripts\run_project.bat`.

## Menu
1. Internet connectivity
2. Gateway connectivity
3. DNS test
4. Latency test
5. IP configuration
6. Routing table
7. Active connections
8. Complete diagnostics
9. Save report
0. Exit

## Project structure
```text
.
├── main.py
├── config.json
├── requirements.txt
├── modules/
│   ├── connectivity.py
│   ├── dns_checker.py
│   ├── latency_monitor.py
│   ├── ip_analyzer.py
│   ├── route_analyzer.py
│   └── connection_monitor.py
├── scripts/
│   ├── network_info.bat
│   ├── diagnostics.ps1
│   └── run_project.bat
├── documentation/
│   ├── Project_Report.md
│   ├── Network_Concepts.md
│   ├── Commands_Reference.md
│   └── Troubleshooting_Guide.md
├── reports/
│   └── sample_report.txt
└── assets/
    └── Architecture.md
```

## Safety & privacy
The toolkit only performs read-only checks and sends simple connectivity/DNS queries. It does not change network settings, scan external hosts, or capture packet contents. Reports can contain local IP addresses and host/network details; review them before publishing.

## Skills demonstrated
Python scripting, Windows command-line tools, TCP/IP fundamentals, DNS, gateway, latency, routing table interpretation, basic troubleshooting, and report generation.
