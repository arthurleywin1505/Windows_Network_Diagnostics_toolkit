# Basic Troubleshooting Guide

## No network access
1. Check adapter status with `Get-NetAdapter` or `ipconfig`.
2. Confirm a valid IPv4 address and subnet mask.
3. Ping the default gateway.
4. Ping a known public IP (if allowed by the network).
5. Test DNS using `nslookup example.com`.
6. Use `tracert` to inspect the path, noting that hops may not respond.

## DNS failure
- Compare name lookup with connectivity to a known IP.
- Review DNS servers shown by `ipconfig /all`.
- DNS queries may be filtered by network policy.

## High or inconsistent latency
- Repeat tests at different times.
- Compare gateway and external target latency.
- Wi-Fi signal/interference, congestion, and routing can affect results.

## Gateway unreachable
- Verify the correct adapter is active.
- Check IP/subnet settings and Wi-Fi/Ethernet link.
- A gateway may block ICMP; corroborate with other checks.

## Safety
Do not change router, firewall, or IP settings without authorization. Escalate persistent issues to the network owner/administrator.
