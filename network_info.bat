@echo off
echo === IP Configuration ===
ipconfig /all
echo.
echo === Route Table ===
route print
echo.
echo === DNS Test ===
nslookup example.com
echo.
echo === Ping Test ===
ping 1.1.1.1
pause
