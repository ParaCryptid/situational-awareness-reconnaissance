# 🤝 Contributing Guide

Welcome to the Training Simulation System!

---

## 🧱 Project Structure

- `src/` – Application logic
- `ci/` – Tests and pipelines
- `build/` – Installer and packaging
- `docs/` – All documentation

---

## 🚀 Getting Started

```bash
git clone https://github.com/paracryptid/training-simulation-system.git
cd training-simulation-system
pip install -r requirements.txt
```

---

## 🧪 Run Tests

```bash
pytest ci/test_suite.py
```

---

## 📦 Build Release

```bash
bash build/build_deb.sh
# or
bash build/build_appimage.sh
```

---

## 📬 Submitting a Pull Request

1. Fork and clone
2. Make your changes
3. Include tests
4. Submit PR with clear summary