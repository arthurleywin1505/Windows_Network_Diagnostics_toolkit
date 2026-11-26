import subprocess, platform

def get_connections():
    cmd = ["netstat", "-ano"] if platform.system() == "Windows" else ["ss", "-tunap"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        lines = (p.stdout or p.stderr).splitlines()
        return {"command": " ".join(cmd), "total_lines": len(lines), "connections": lines[:60]}
    except Exception as exc:
        return {"status": "ERROR", "detail": str(exc)}
