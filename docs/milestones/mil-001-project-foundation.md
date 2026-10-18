# Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether the repository has the configuration, structure and documentation skeleton that every later gateway builds on: a Python 3.13 project with a local `.venv`, pytest, constants, Doxygen and a public description.

## Deliverable

A pull request that adds `pyproject.toml`, `.gitignore`, the package skeleton `src/quizzler/` with `constants.py`, the folder `tests/` with a passing smoke test, the `Doxyfile`, a first `README.md` from the framework template with `.venv` setup instructions, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python = ">=3.13"` and an empty `dependencies` list | Both present | Either missing |
| 2 | A fresh `.venv` can be created and `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed | Commands succeed | Any command fails |
| 3 | `python -m pytest` passes | 0 failures | Any failure |
| 4 | `.gitignore` ignores `.venv/`, `__pycache__/` and `.env`, and `git status` shows no `.env` | All three ignored | Any missing |
| 5 | `Doxyfile` exists and `doxygen` is documented in the README | Present | Missing |
| 6 | The repository has a description and at least five topics on the git host | Both set | Either unset |
| 7 | `bash framework/scripts/check-readme.sh` passes | Exit 0 | Non-zero |
| 8 | Python code has a `Go` review record against `QC-PY-001` | `Go` | Anything else |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; it needs only the accepted baseline (Business Case, Stakeholder Analysis, Project Plan) |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O5, O6, O7 | [BC-001] |
| SC5, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — within the Business Case window of 2026-10-18 to 2026-10-25.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Declare the project with `requires-python = ">=3.13"`, an empty runtime `dependencies` list, a `dev` extra with pytest, pytest-cov, ruff and mypy, the `src` layout and the pytest configuration. This keeps the runtime free of dependencies for S03. | No | ADR-0001 |
| 2 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv/`, `.env`, build output and Doxygen output, so tokens and environments are never committed. | No | |
| 3 | Create package skeleton and constants.py | Create `src/quizzler/` with the layer packages `domain`, `application`, `infrastructure`, `presentation`, and `constants.py` with the first constants (API URL, question count, colours, fonts). Add `tests/unit`, `tests/integration` and a smoke test so pytest runs. | No | ADR-0001 |
| 4 | Add Doxyfile | Add a `Doxyfile` for the Python sources (`OPTIMIZE_OUTPUT_JAVA`, input `src/`, output `build/doxygen`) and the Doxygen comment style used in the source. | No | |
| 5 | Write README with venv setup | Write `README.md` from the framework template with the `.venv` creation, `python -m pip install --upgrade pip`, install, run and test instructions for Windows and POSIX shells. Screenshots are added in MIL-004. | No | |
| 6 | Set repository description and topics | Set the description and topics of the repository on the git host through its API, using the token in the git-ignored `.env`. The token is never printed, imported by the project or tested. | No | |

---

[BC-001]: ../business-case.md
