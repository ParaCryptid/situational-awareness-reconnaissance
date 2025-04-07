
import os
import time
import json
from datetime import datetime

SENSOR_LOG = "/opt/training-system/logs/sensor_feed.json"
REPORTS_DIR = "/opt/training-system/reports"

def generate_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"recon_report_{now}.txt")

    if not os.path.exists(SENSOR_LOG):
        print("[AI RECON] No sensor data found.")
        return

    lines = []
    with open(SENSOR_LOG, "r") as f:
        for line in f.readlines()[-10:]:  # last 10 entries
            data = json.loads(line)
            lines.append(f"- At {datetime.fromtimestamp(data['timestamp'])}: "
                         f"Radiation={data['radiation']} µSv/h, "
                         f"BioAgent={data['bio_agent']}, "
                         f"ChemLevel={data['chem_level']} ppm, "
                         f"GPS=({data['gps']['lat']}, {data['gps']['lon']})")

    with open(report_path, "w") as out:
        out.write("INTELLIGENCE RECON REPORT\n")
        out.write("===========================\n\n")
        for l in lines:
            out.write(l + "\n")

    print(f"[AI RECON] Report generated: {report_path}")
