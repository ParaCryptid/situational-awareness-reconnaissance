# 📘 Field Guide – Training Simulation System

## 🧭 Introduction
This guide helps field operators, analysts, or trainers effectively use the simulation system in real-world or training environments.

---

## 🚦 Quick Start (Live Ops)
```bash
./training_simulation_system --simulate
```

## 🎛️ Mode Descriptions

| Mode        | Command                     | Purpose                          |
|-------------|-----------------------------|----------------------------------|
| Simulate    | `--simulate`                | Run a preloaded scenario         |
| Replay      | `--replay <file>`           | Replay a saved log               |
| View Logs   | `--logview`                 | Navigate past session logs       |

---

## 🛠️ Configuration

Located at: `config.yaml` (generated on first run)

You can configure:
- Simulation speed
- Log location
- Offline toggle
- Auto-start behavior

---

## 💾 Saving & Exporting

Logs are stored in:
```
~/.simulation/logs/YYYY-MM-DD/
```

Export manually or set up `rsync` or USB autosync for backup.

---

## 🛡️ Offline Safety

This system:
- Runs with no internet required
- Performs no telemetry
- Auto-secures logs on exit