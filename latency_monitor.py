import subprocess, platform, re
from statistics import mean

def measure_latency(host, count=4, timeout_ms=1500):
    if not host:
        return {"status": "ERROR", "detail": "No target specified."}
    cmd = ["ping", "-n", str(count), "-w", str(timeout_ms), host] if platform.system() == "Windows" else ["ping", "-c", str(count), "-W", str(max(1, timeout_ms//1000)), host]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=count*(timeout_ms/1000)+5)
        output = proc.stdout or proc.stderr
        values = [float(x) for x in re.findall(r"time[=<]\s*([\d.]+)\s*ms", output, flags=re.I)]
        if values:
            return {"target": host, "status": "MEASURED", "samples_ms": values, "average_ms": round(mean(values), 2), "min_ms": min(values), "max_ms": max(values)}
        return {"target": host, "status": "NO_REPLY", "output": output.strip()}
    except Exception as exc:
        return {"target": host, "status": "ERROR", "detail": str(exc)}
