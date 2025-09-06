#!/usr/bin/env python3
"""
TryHuntMe - CLI learning toolkit for bug hunting (educational, local use only)
Author / Copyright: KalloloCoder
"""

import sys
import os
import argparse
import time
import threading
import webbrowser
from colorama import init as colorama_init, Fore, Style
from tqdm import tqdm
from modules import recon, poc
from subprocess import Popen
import signal

colorama_init(autoreset=True)

APP_NAME = "TryHuntMe"
COPYRIGHT = "© KalloloCoder"
PID_FILE = os.path.join(os.path.dirname(__file__), "vuln_server.pid")

ASCII = r"""
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████████████▓▒░░▒▓████████▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░
"""

def colorful_print(s, color=Fore.GREEN):
    print(color + s + Style.RESET_ALL)

def loading_effect(message="Loading", seconds=2):
    for _ in range(seconds):
        for ch in "|/-\\":
            print(f"\r{Fore.GREEN}{message} {ch}{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.12)
    print("\r" + " " * (len(message) + 4), end="\r")

def progress_bar_demo(total=30, desc="Processing"):
    for _ in tqdm(range(total), desc=desc, ncols=60):
        time.sleep(0.03)

def start_vuln_server(port=8000, open_browser=False):
    colorful_print("[*] Starting local vulnerable server (for training) ...", Fore.CYAN)
    loading_effect("Booting server", 2)
    path = os.path.join(os.path.dirname(__file__), "vuln_server.py")
    if not os.path.exists(path):
        colorful_print("[!] vuln_server.py not found!", Fore.RED)
        return
    # Start server as subprocess and save PID
    proc = Popen([sys.executable, path, str(port)])
    with open(PID_FILE, "w") as f:
        f.write(str(proc.pid))
    colorful_print(f"[+] Vulnerable server running on http://127.0.0.1:{port}", Fore.GREEN)
    if open_browser:
        webbrowser.open(f"http://127.0.0.1:{port}")

def stop_vuln_server():
    if not os.path.exists(PID_FILE):
        colorful_print("[!] No running server found.", Fore.YELLOW)
        return
    with open(PID_FILE, "r") as f:
        pid = int(f.read().strip())
    try:
        os.kill(pid, signal.SIGTERM)
        colorful_print(f"[+] Server with PID {pid} stopped.", Fore.GREEN)
        os.remove(PID_FILE)
    except Exception as e:
        colorful_print(f"[!] Failed to stop server: {e}", Fore.RED)

def run_recon(args):
    colorful_print("[*] Reconnaissance module", Fore.CYAN)
    loading_effect("Gathering info", 2)
    if args.host:
        start = args.start if args.start else 1
        end = args.end if args.end else 1024
        recon.port_scan(args.host, start, end, threads=args.threads, timeout=args.timeout)
    else:
        colorful_print("[!] Provide a host (IP or domain) with -t/--target", Fore.YELLOW)

def run_poc(args):
    colorful_print("[*] PoC Generator module", Fore.CYAN)
    loading_effect("Preparing PoC", 1)
    template = poc.generate_poc(args.type or "xss", args.target or "http://127.0.0.1")
    colorful_print("=== PoC ===", Fore.MAGENTA)
    print(template)
    if args.obfuscate:
        colorful_print("[*] Obfuscating payload ...", Fore.CYAN)
        ob = poc.obfuscate_js(template)
        colorful_print("--- Obfuscated ---", Fore.MAGENTA)
        print(ob)

def make_report(args):
    colorful_print("[*] Report Generator (simple markdown)", Fore.CYAN)
    lines = []
    lines.append(f"# TryHuntMe Report\n")
    lines.append(f"Target: {args.target}\n")
    lines.append("## Findings\n\n- No automated findings in demo (use modules to fill this)\n")
    out = args.output or "tryhuntme_report.md"
    with open(out, "w") as f:
        f.writelines([l if l.endswith("\n") else l + "\n" for l in lines])
    colorful_print(f"[+] Report saved to {out}", Fore.GREEN)

def show_banner():
    print(Fore.GREEN + ASCII + Style.RESET_ALL)
    print(f"{Fore.CYAN}{APP_NAME} - Learn Bug Hunting Locally{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{COPYRIGHT}{Style.RESET_ALL}\n")

def main():
    show_banner()

    parser = argparse.ArgumentParser(
        prog="tryhuntme",
        description="TryHuntMe — educational bug hunting toolkit (local only).",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Contoh pemakaian:
  tryhuntme start-server --port 8080 --open
  tryhuntme stop-server
  tryhuntme recon -t 192.168.1.10 --start 20 --end 1000
  tryhuntme poc --type xss --target http://example.com --obfuscate
  tryhuntme report --target example.com -o myreport.md
"""
    )

    sub = parser.add_subparsers(dest="cmd")

    # start-server
    s_srv = sub.add_parser("start-server", help="Start the local vulnerable server for testing")
    s_srv.add_argument("--port", "-p", type=int, default=8000, help="Port to run local server")
    s_srv.add_argument("--open", action="store_true", help="Open in browser after start")

    # stop-server
    s_stop = sub.add_parser("stop-server", help="Stop the running vulnerable server")

    # recon
    s_recon = sub.add_parser("recon", help="Reconnaissance: basic port scan and DNS resolve")
    s_recon.add_argument("-t", "--target", dest="host", help="Target host (ip or domain)")
    s_recon.add_argument("--start", type=int, help="Start port")
    s_recon.add_argument("--end", type=int, help="End port")
    s_recon.add_argument("--threads", type=int, default=50, help="Threads for scan")
    s_recon.add_argument("--timeout", type=float, default=1.0, help="Socket timeout seconds")

    # poc
    s_poc = sub.add_parser("poc", help="Generate a simple PoC payload")
    s_poc.add_argument("--type", choices=["xss", "sqli"], help="Type of PoC")
    s_poc.add_argument("--target", help="Target base URL")
    s_poc.add_argument("--obfuscate", action="store_true", help="Return obfuscated payload")

    # report
    s_rep = sub.add_parser("report", help="Generate a simple markdown report")
    s_rep.add_argument("--target", required=True)
    s_rep.add_argument("--output", "-o", help="Output file name")

    # info
    s_info = sub.add_parser("about", help="About TryHuntMe")

    # global help/style examples
    parser.add_argument("-v", "--version", action="store_true", help="Show version info")
    args = parser.parse_args()

    if args.version:
        colorful_print(f"{APP_NAME} v0.9.0", Fore.CYAN)
        sys.exit(0)

    if args.cmd == "start-server":
        start_vuln_server(port=args.port, open_browser=args.open)
    elif args.cmd == "stop-server":
        stop_vuln_server()
    elif args.cmd == "recon":
        run_recon(args)
    elif args.cmd == "poc":
        run_poc(args)
    elif args.cmd == "report":
        make_report(args)
    elif args.cmd == "about":
        colorful_print(f"{APP_NAME} — educational local bug hunting toolkit", Fore.CYAN)
        print("Modules available: recon, poc, server, report")
        print("Designed for local training only.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
