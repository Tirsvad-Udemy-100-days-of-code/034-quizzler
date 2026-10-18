🌐 [English](Testing) · **Dansk** · [Bahasa Melayu](Testing-ms)

# Test

Kør disse fra repositoryets rod med `.venv` aktivt:

```bash
python -m pytest
python -m pytest --cov=quizzler
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src tests
doxygen Doxyfile
```

Testene bruger falske erstatninger og kræver intet netværk. Den ene GUI-røgtest opretter et rigtigt vindue og springes over, hvis der ikke er en skærm. Doxygen skriver API-dokumentationen til `doxygen/html`.
