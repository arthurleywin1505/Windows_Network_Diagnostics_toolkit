import socket

def check_dns(host):
    try:
        answers = sorted({item[4][0] for item in socket.getaddrinfo(host, None)})
        return {"host": host, "status": "SUCCESS", "addresses": answers}
    except socket.gaierror as exc:
        return {"host": host, "status": "FAILED", "detail": str(exc)}
    except Exception as exc:
        return {"host": host, "status": "ERROR", "detail": str(exc)}
