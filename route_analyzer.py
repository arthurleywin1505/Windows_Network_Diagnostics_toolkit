import subprocess, platform

def get_routes():
    cmd = ["route", "print"] if platform.system() == "Windows" else ["ip", "route"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return {"command": " ".join(cmd), "output": (p.stdout or p.stderr).strip()}
    except Exception as exc:
        return {"status": "ERROR", "detail": str(exc)}
