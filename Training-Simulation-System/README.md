# 🛰️ Training Simulation System

**Author:** ParaCryptid  
**Version:** 1.0.0  
**License:** MIT  
**Status:** Fully Cross-Platform & Production-Ready  
**Use Case:** Real-time training simulation system for field exercises, scenario drills, and secure offline simulation.

---

## 🚀 Overview

This is a secure, plug-and-play training simulation platform built for cross-platform deployment on:
- Windows (.exe)
- Ubuntu/Debian (.deb)
- Linux portable (.AppImage)

Ideal for:
- Simulation training
- Field exercises
- Operational preparation

---

## ✅ Features

- 🧠 Simulation replay, record, and log view modes
- 🌐 Flask-based lightweight backend
- 📦 Cross-platform packaging (.deb, .exe, .AppImage)
- 🔐 Hardened for safe offline environments
- 🧰 CLI, TUI fallback, and GUI-ready architecture
- ⚙️ CI/CD auto-tests, build, and deploy

---

## 📦 Installation

### 🔧 Python (Developer)
```bash
git clone https://github.com/paracryptid/training-simulation-system.git
cd training-simulation-system
pip install -r requirements.txt
python src/main.py
```

### 🐧 Linux (.deb)
```bash
sudo dpkg -i build/training-simulation-system.deb
```

### 🪟 Windows (.exe)
Run `build/training_simulation_system.exe`

### 🧳 Portable Linux (.AppImage)
```bash
chmod +x build/training_simulation_system.AppImage
./build/training_simulation_system.AppImage
```

---

## 🛡️ Security

This project is hardened for field usage with:
- No outbound traffic
- No telemetry
- Local-only operations
- Log sanitization and rotation
- Self-contained mode

---

## 🧪 Testing & CI/CD

All changes trigger:
- ✅ Code linting
- ✅ Unit tests
- ✅ Build for all OS targets
- ✅ Release packaging

---

## 👨‍✈️ Operational Modes

- `--simulate` → run a recorded scenario
- `--replay` → replay saved logs
- `--logview` → browse operational logs

---

## 📖 Field Guide

For full usage, refer to [`docs/FIELD_GUIDE.md`](docs/FIELD_GUIDE.md)

---

## 🤝 Contributing

Contributions welcome! See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)

---

## 📜 License

MIT License. Safe for civilian, academic, or defense-grade simulation environments.