🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install-ms)

# Installation

## Krav

- Python 3.13 eller nyere med Tkinter (på Debian og Ubuntu: `sudo apt install python3-tk`).
- Ingen eksterne afhængigheder ved kørsel. `pytest`, `ruff` og `mypy` er kun udviklingsværktøjer.

## Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux og macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

`python -m pip install --upgrade pip` opgraderer pip i `.venv`. Mappen `.venv` ignoreres af git.
