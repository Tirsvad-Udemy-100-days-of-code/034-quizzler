🌐 [English](Testing) · [Dansk](Testing-da) · **Bahasa Melayu**

# Ujian

> Nota: terjemahan Bahasa Melayu ini belum disemak oleh penutur asli; bahasa Inggeris ialah teks rasmi.

Jalankan arahan ini dari akar repositori dengan `.venv` aktif:

```bash
python -m pytest
python -m pytest --cov=quizzler
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src tests
doxygen Doxyfile
```

Ujian menggunakan pengganti palsu dan tidak memerlukan rangkaian. Satu ujian asap GUI mencipta tetingkap sebenar dan dilangkau jika tiada paparan. Doxygen menulis dokumentasi API ke `doxygen/html`.
