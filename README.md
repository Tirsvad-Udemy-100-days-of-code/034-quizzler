# 🚀 Quizzler

A desktop true/false quiz built with Tkinter that fetches its questions from the Open Trivia Database; it is the Day 34 project of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants and anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

Quizzler shows one true/false question at a time, checks your answer when you press the True or False button, and keeps your score. Questions come from the Open Trivia Database API, with HTML entities such as `&quot;` turned into readable text.

![Quizzler showing a question][screenshot-question]

The repository is laid out in layers under `src/quizzler/`:

| Folder | What it holds |
| --- | --- |
| `domain/` | `Question` and `QuizBrain` (the course's `question_model.py` and `quiz_brain.py`) |
| `application/` | The `QuestionSource` port and the use case that builds the question bank |
| `infrastructure/` | The Open Trivia Database client (standard library only) |
| `presentation/` | The Tkinter `QuizInterface` (the course's `ui.py`) and its view model |
| `constants.py` | All constants (API URL, colours, fonts) |
| `main.py` | The entry point that wires the layers together |

The course's `data.py` is replaced by the API client, and its `question_data` by the records the API returns. The wiki ([English][wiki], [Dansk][wiki-da], [Bahasa Melayu][wiki-ms]) explains the mapping in more detail.

Tests are in `tests/`, project documents in `docs/`. The code has Doxygen comments and a `Doxyfile`.

## 📋 Requirements

- Python 3.13 or later, with Tkinter (included in the Windows and macOS installers; on Debian and Ubuntu install `python3-tk`).
- `venv` to create a local virtual environment.
- No third-party runtime dependencies. `pytest` (and optionally `ruff`, `mypy`) are installed only for development.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the API documentation.

## 🛠️ Setup

Create and activate a local `.venv`, then upgrade pip and install the project with its development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

With the `.venv` active:

```bash
python -m quizzler
```

An internet connection is needed to fetch the questions. Press the green check for True and the red cross for False: the question box turns green for a right answer and red for a wrong one.

| Right answer | Wrong answer |
| --- | --- |
| ![Right answer][screenshot-right] | ![Wrong answer][screenshot-wrong] |

If the question service cannot be reached, a window with a short message is shown and the program exits with code 1.

## 🧪 Tests

```bash
python -m pytest
```

The tests use fakes and need no network. To see coverage: `python -m pytest --cov=quizzler`. To build the API documentation: `doxygen Doxyfile` (output in `doxygen/html`).

## 📄 License

GNU Affero General Public License v3, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Governance][GOV-001] | The review workflow, who decides and how disputes escalate |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[license]: ./LICENSE
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/issues
[screenshot-question]: ./docs/images/question.png
[screenshot-right]: ./docs/images/right-answer.png
[screenshot-wrong]: ./docs/images/wrong-answer.png
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/wiki
[wiki-da]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/wiki/Home-da
[wiki-ms]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/wiki/Home-ms
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[GOV-001]: ./docs/sqa/governance.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
