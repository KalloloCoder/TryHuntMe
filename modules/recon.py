# modules/recon.py
import socket
import threading
import sys
from colorama import Fore, Style

def _banner(s):
    try:
        s.settimeout(1.0)
        b = s.recv(1024)
        return b.decode(errors="ignore").strip()
    except Exception:
        return ""

def _scan_port(host, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        banner = _banner(s)
        print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port} - Banner: {banner}")
        s.close()
        return True
    except Exception:
        return False

def port_scan(host, start=1, end=1024, threads=50, timeout=0.8):
    print(f"[+] Scanning {host} ports {start}-{end} (threads={threads})")
    ports = list(range(start, end+1))
    lock = threading.Lock()
    def worker():
        while True:
            lock.acquire()
            if not ports:
                lock.release()
                return
            p = ports.pop(0)
            lock.release()
            _scan_port(host, p, timeout)

    workers = []
    for _ in range(min(threads, len(ports))):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        workers.append(t)
    for w in workers:
        w.join()
    print("[+] Scan complete.")
