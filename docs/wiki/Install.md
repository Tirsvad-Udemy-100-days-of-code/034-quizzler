🌐 **English** · [Dansk](Install-da) · [Bahasa Melayu](Install-ms)

# Install

## Requirements

- Python 3.13 or later with Tkinter (on Debian and Ubuntu: `sudo apt install python3-tk`).
- No third-party runtime dependencies. `pytest`, `ruff` and `mypy` are development tools only.

## Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux and macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

`python -m pip install --upgrade pip` upgrades pip inside the `.venv`. The `.venv` folder is ignored by git.
