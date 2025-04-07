@echo off
REM PyInstaller-based Windows .exe build script
pip install pyinstaller
pyinstaller --onefile src/main.py --name training_simulation_system
move dist\training_simulation_system.exe build\training_simulation_system.exe