🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

# Pemasangan

> Nota: terjemahan Bahasa Melayu ini belum disemak oleh penutur asli; bahasa Inggeris ialah teks rasmi.

## Keperluan

- Python 3.13 atau lebih baharu dengan Tkinter (pada Debian dan Ubuntu: `sudo apt install python3-tk`).
- Tiada kebergantungan pihak ketiga semasa dijalankan. `pytest`, `ruff` dan `mypy` hanya alat pembangunan.

## Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux dan macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

`python -m pip install --upgrade pip` menaik taraf pip di dalam `.venv`. Folder `.venv` diabaikan oleh git.
