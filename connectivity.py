import subprocess
import platform

def check_ping(host, count=4, timeout_ms=1500):
    if not host:
        return {"status": "UNKNOWN", "detail": "Gateway address could not be detected."}
    count = max(1, int(count))
    timeout_ms = max(500, int(timeout_ms))
    cmd = ["ping", "-n", str(count), "-w", str(timeout_ms), host] if platform.system() == "Windows" else ["ping", "-c", str(count), "-W", str(max(1, timeout_ms//1000)), host]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=count*(timeout_ms/1000)+5)
        text = (proc.stdout or proc.stderr).strip()
        return {"target": host, "status": "REACHABLE" if proc.returncode == 0 else "UNREACHABLE", "output": text}
    except Exception as exc:
        return {"target": host, "status": "ERROR", "detail": str(exc)}
