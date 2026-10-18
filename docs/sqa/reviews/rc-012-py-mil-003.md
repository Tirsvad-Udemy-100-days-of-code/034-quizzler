# RC-012: Python source of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: Python source of MIL-003 (presentation, main, tests)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)
- Design reference: [ADR-0001]

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Classes `QuizInterface`, `QuizViewModel`; modules and functions snake_case; constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Course names kept (`get_next_question`, `true_pressed`, `false_pressed`); names follow DICT-001. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; mypy --strict reports no issues in 25 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `main` catches only `QuestionSourceError`; no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files opened; images are loaded by tkinter from a package path. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public classes and methods have Doxygen docstrings; private view helpers are short and doxygen reports 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` or logging; no secrets; `.env` is not read. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | `QuizInterface` is the view and `QuizViewModel` the view model of ADR-0001; `main.py` is the composition root. Extra `show_error` function is a recorded deviation: the error window is part of the view. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 47 tests, headless apart from the e2e smoke test that skips without a display; no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` clean. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Standard library only; `dependencies = []`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | All colours, fonts, sizes, texts defined once in `constants.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `presentation` imports `domain` and constants; `domain` does not import presentation; `main.py` imports presentation lazily; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | The view model holds the state, the view only draws; `main` receives its source and callables by injection. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `presentation` package, `main.py` as composition root; tests in `tests/unit/presentation`, `tests/unit`, `tests/e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case names; `images/true.png`, `images/false.png`. |

## Overall Verdict

Go — every Mandatory criterion passes; ruff, ruff format, mypy --strict and pytest were run on the reviewed files.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None: no Fail | S01 | 2026-10-25 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-architecture-and-dependencies.md
