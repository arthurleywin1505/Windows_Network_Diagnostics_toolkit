# Project Report

## Title
Windows Network Diagnostics & Monitoring Toolkit

## Abstract
This project is a small Windows-oriented utility that brings common network diagnostic checks into a single menu-driven Python program. It combines built-in Windows command-line utilities with Python's standard library to check connectivity, DNS resolution, latency, IP configuration, routing information, and active connections.

## Problem Statement
When users experience connectivity problems, an administrator often runs several commands manually. This project organizes those checks and saves their results in a text report to support faster initial troubleshooting.

## Objectives
- Verify basic host reachability.
- Test DNS name resolution.
- Measure ping response latency where replies are available.
- Collect IP configuration and routing information.
- Display active connection information.
- Save diagnostic results for review.

## Design
The menu interface in `main.py` calls separate modules. Each module performs one diagnostic task. The scripts folder contains optional Windows batch and PowerShell helpers.

## Modules
- Connectivity: ICMP ping check
- DNS: hostname lookup using Python socket
- Latency: ping samples and response-time summary
- IP analyzer: `ipconfig /all` capture
- Route analyzer: `route print` capture
- Connection monitor: `netstat -ano` capture

## Testing
Run the application on a Windows machine and select individual checks or the complete diagnostic option. Results are environment-dependent. Save a report and review it before sharing; it may include private IP addresses, host names, routes, and connection details.

## Limitations
- ICMP may be blocked by a firewall or destination; ping failure does not always prove that a host is down.
- It is a basic troubleshooting tool, not a full enterprise monitoring platform.
- The application does not modify network configuration.
- No live testing is claimed by the included illustrative sample.

## Conclusion
The toolkit demonstrates practical Windows networking knowledge and Python automation for common first-line diagnostics.
