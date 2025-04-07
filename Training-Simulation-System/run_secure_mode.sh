#!/bin/bash

echo "[+] Starting Secure Training Simulation System..."
python3 -m src.sensor_simulation.simulator & 
python3 -m src.dropzone_handler.watcher & 
python3 -m src.watchdog.monitor & 
python3 -m src.ai_recon.recon &

echo "[+] All services launched."
