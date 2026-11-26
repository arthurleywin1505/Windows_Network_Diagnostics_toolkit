# Read-only Windows network diagnostics
Write-Host "=== IP Configuration ===" -ForegroundColor Cyan
Get-NetIPConfiguration | Format-List
Write-Host "=== Network Adapters ===" -ForegroundColor Cyan
Get-NetAdapter | Format-Table -AutoSize
Write-Host "=== DNS Client Cache (summary) ===" -ForegroundColor Cyan
Get-DnsClientCache | Select-Object -First 15 | Format-Table -AutoSize
Write-Host "=== Route Table ===" -ForegroundColor Cyan
Get-NetRoute -AddressFamily IPv4 | Sort-Object RouteMetric | Select-Object -First 25 | Format-Table -AutoSize
Write-Host "=== TCP Connections (sample) ===" -ForegroundColor Cyan
Get-NetTCPConnection -State Established -ErrorAction SilentlyContinue | Select-Object -First 25 | Format-Table -AutoSize
