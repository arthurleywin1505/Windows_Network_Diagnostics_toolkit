import subprocess, platform, re

def get_ip_config():
    cmd = ["ipconfig", "/all"] if platform.system() == "Windows" else ["ip", "addr"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        output = p.stdout or p.stderr
        if platform.system() != "Windows":
            return {"raw_output": output.strip()}
        # Extract commonly useful fields from Windows output (first suitable active adapter).
        fields = {}
        patterns = {
            "hostname": r"Host Name\\s*\\.\\s*:\\s*(.+)",
            "adapter": r"adapter ([^:]+):",
            "ipv4": r"IPv4 Address[^:]*:\\s*([\\d.]+)",
            "subnet_mask": r"Subnet Mask[^:]*:\\s*([\\d.]+)",
            "gateway": r"Default Gateway[^:]*:\\s*([\\d.]+)"
        }
        for key, pat in patterns.items():
            m = re.search(pat, output, re.I)
            if m:
                fields[key] = m.group(1).strip().replace("(Preferred)", "")
        fields["raw_output"] = output.strip()
        return fields
    except Exception as exc:
        return {"status": "ERROR", "detail": str(exc)}
