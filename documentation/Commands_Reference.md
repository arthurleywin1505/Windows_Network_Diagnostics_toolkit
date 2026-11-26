# Windows Commands Reference

| Command | Purpose |
|---|---|
| `ipconfig /all` | Detailed interface/IP/DNS/gateway information |
| `ping 1.1.1.1` | Test reachability using ICMP |
| `ping -n 4 1.1.1.1` | Send four echo requests |
| `tracert example.com` | Show hops toward a destination |
| `nslookup example.com` | Query DNS |
| `route print` | Display IPv4/IPv6 route tables |
| `netstat -ano` | Show connections/listeners with PID |
| `Get-NetIPConfiguration` | PowerShell IP configuration |
| `Get-NetAdapter` | PowerShell network adapter status |
| `Get-NetRoute` | PowerShell route information |
| `Get-NetTCPConnection` | PowerShell TCP connection details |

Commands in this project are used for observation/diagnostics only. Avoid publishing output containing private network information.
