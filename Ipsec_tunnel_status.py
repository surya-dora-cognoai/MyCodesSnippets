import telnetlib
import subprocess
import time

# Configuration
HOST = "10.200.15.249"
PORT = 7003
IPSEC_CONNECTION = "tct10"

def check_telnet(host, port, timeout=5):
    try:
        with telnetlib.Telnet(host, port, timeout):
            print(f"[OK] Telnet to {host}:{port} is working.")
            return True
    except Exception as e:
        print(f"[ERROR] Telnet to {host}:{port} failed: {e}")
        return False

def restart_ipsec(connection_name):
    print(f"[INFO] Restarting IPsec connection: {connection_name}")
    try:
        subprocess.run(["sudo", "ipsec", "down", connection_name], check=True)
        time.sleep(2)
        subprocess.run(["sudo", "ipsec", "up", connection_name], check=True)
        print(f"[SUCCESS] IPsec tunnel {connection_name} restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to restart IPsec: {e}")


def main():
    if not check_telnet(HOST, PORT):
        restart_ipsec(IPSEC_CONNECTION)


main()
