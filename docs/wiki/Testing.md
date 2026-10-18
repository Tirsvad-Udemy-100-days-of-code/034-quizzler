🌐 **English** · [Dansk](Testing-da) · [Bahasa Melayu](Testing-ms)

# Testing

Run these from the repository root with the `.venv` active:

```bash
python -m pytest
python -m pytest --cov=quizzler
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src tests
doxygen Doxyfile
```

The tests use fakes and need no network. The one GUI smoke test creates a real window and is skipped when no display is available. Doxygen writes the API documentation to `doxygen/html`.
