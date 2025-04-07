
import subprocess
import time

SERVICES = ["dropzone", "sensor", "ai", "gui"]

def restart_service(service_name):
    try:
        subprocess.run(["systemctl", "restart", service_name], check=True)
        print(f"[WATCHDOG] Restarted {service_name}")
    except Exception as e:
        print(f"[WATCHDOG] Failed to restart {service_name}: {str(e)}")

def monitor_services():
    while True:
        for svc in SERVICES:
            result = subprocess.run(["systemctl", "is-active", svc], capture_output=True, text=True)
            if "inactive" in result.stdout or "failed" in result.stdout:
                restart_service(svc)
        time.sleep(30)
