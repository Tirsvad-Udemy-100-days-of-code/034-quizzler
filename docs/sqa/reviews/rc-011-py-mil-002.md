# RC-011: Python source of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0f8ab48] |

---

## Artifact Under Review

- Instance reviewed: Python source of MIL-002 (domain, application, infrastructure, tests)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)
- Design reference: [ADR-0001]

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions, variables snake_case; classes `Question`, `QuizBrain`, `OpenTriviaClient`; errors end in `Error`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow DICT-001 (`Question`, `QuizBrain`, `answer`, `score`, `question_list`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated including `-> None`; verified by mypy --strict. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; `QuestionSourceError` raised `from err` in the client and the use case. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (the default opener is a function); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | `urlopen` used in a `with` block. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings state what, with Doxygen `@brief`, `@param`, `@return`, `@throws`; `doxygen Doxyfile` has no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging needed; no secrets read. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | `Question`, `QuizBrain`, `QuestionSource`, `OpenTriviaClient` implement the layout of ADR-0001; the extra `NoCurrentQuestionError` and `QuizFinishedError` are recorded here as a deviation. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 34 tests with fakes, no network, named for behaviour. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` reports no issues in 18 files. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; only the standard library is imported. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Record keys and constants defined once (`constants.py`, module-private keys in the use case). |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing outside itself; `application` imports `domain`; `infrastructure` imports `application`; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `QuizBrain` has one reason to change; the client depends on an injected opener; use case depends on the `QuestionSource` protocol. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure` packages with tests in `tests/unit` and `tests/integration`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case file names without spaces. |

## Overall Verdict

Go — every Mandatory criterion passes; ruff, ruff format, mypy --strict and pytest were run on the reviewed files.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None: no Fail | S01 | 2026-10-25 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-architecture-and-dependencies.md
[0f8ab48]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/0f8ab48feaaf83deb905fc58edad911dc9a619d2
