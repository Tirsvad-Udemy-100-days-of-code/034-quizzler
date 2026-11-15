# Business Case: Quizzler

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [2133243] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added objective O8, success criterion SC9, a scope item, an out-of-scope item, a risk and constraints for the baseline milestone MIL-005; changed SC8 to five milestones; set the domain to education; reviewed in autonomous mode, not independent | [77b48ec] |

---

## Executive Summary

Quizzler is a desktop true/false quiz application built as the Day 34 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It replaces a text-based quiz with hard-coded questions by a graphical interface (Tkinter) that fetches fresh trivia questions from the Open Trivia Database API, shows them one at a time and checks each answer against the correct one. The project is also a worked example of a documented, reviewed and tested Python repository that other course participants (S02) and repository visitors (S03) can read and run. We propose to build it in four reviewed gateways.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (artifact chain Business Case, Stakeholder Analysis, Project Plan, milestones, tasks, code; every step ends with a review record). Quality attributes follow ISO/IEC 25010:2023. Code follows PEP 8, PEP 257 and PEP 484, and a Clean Architecture layering with the presentation pattern MVVM for a user interface. Requirements come from the course assignment (the Day 34 lectures) rather than from use-case modelling, which is out of proportion for an assignment of this size.

## Problem Statement

The course starter code asks questions from a fixed list in `data.py`, so the quiz is the same every run and runs only in a console. Participants who finish the assignment seldom publish a result that others can run: there is often no setup guide, no tests, no stated Python version and no explanation of how the API response (with HTML entities such as `&quot;`) is handled.

## Business Opportunity

A small, well-documented reference solution lets S02 compare their own solutions with readable code that keeps the assignment's names (`Question`, `QuizBrain`, `QuizInterface`, `question_data`, `true_pressed`, `false_pressed`, `check_answer`), and lets S03 find a clean example repository with a description, topics and README. For S01 it is evidence of the practices the course teaches (API requests, typing, OOP, GUI) applied with tests and documentation.

## Objectives

| # | Objective |
| --- | --- |
| O1 | The application fetches true/false questions from the Open Trivia Database API (URL parameters for the number of questions and the type) and unescapes HTML entities before showing them. |
| O2 | The application shows each question in a Tkinter window with a score label, a canvas and true/false image buttons, and ends when the questions are used up. |
| O3 | The `true_pressed` and `false_pressed` methods of the interface call `check_answer` of the quiz logic with the user's answer, and the answer is checked against the correct one from the API. The user-visible feedback follows in a later lecture and is part of O2's scope as right/wrong feedback and score. |
| O4 | The code is typed, documented with Doxygen comments, uses `constants.py` for constants and is covered by pytest tests that need no network. |
| O5 | A newcomer can create a local `.venv`, upgrade pip, run the app and the tests from the README alone. |
| O6 | The repository has a description, topics, a README with a screenshot and a wiki in English, Danish and Bahasa Malaysia. |
| O7 | Every step is traceable: each gateway is a reviewed milestone with tasks as issues, delivered by one pull request. |
| O8 | The finished project is brought to the common baseline of the framework: the adopted framework release, the wiki sidebar in the framework's shape, complete licence metadata and review records for every changed document ([MIL-005]). |

## Scope

### In Scope

- The Quizzler application: question model, quiz logic, API client, Tkinter interface, entry point, with the assignment's function and class names.
- Answer checking from the buttons (`true_pressed`, `false_pressed`, `check_answer`) and right/wrong feedback and score in the window.
- Project configuration (`pyproject.toml`, Python 3.13 or later, `.gitignore`, `Doxyfile`, `constants.py`) and the folder structure `src/`, `tests/`, `docs/`.
- pytest tests, run from a local `.venv`.
- README from the framework template, with instructions for running the app and the tests, and a screenshot.
- Wiki pages in English, Danish and Bahasa Malaysia, with screenshots.
- Repository description and topics on the git host.
- The baseline milestone [MIL-005]: the framework release, the wiki sidebar in the framework's shape, the README without the private framework files in its appendix, licence and project URL metadata, `.editorconfig`, `.env.example`, review records and a current traceability matrix. It changes no behaviour of the program.

### Out of Scope

- Question categories, difficulty selection, multiple-choice questions, timers or persistent high scores.
- Packaging for PyPI or an installer.
- Runtime dependencies (the standard library is enough).
- Automated GUI tests and CI pipelines (a later extension).
- Any change to `src/` or `tests/` in the baseline milestone [MIL-005].

## Expected Benefits

### Tangible Benefits

- A runnable application and a passing test suite.
- A README and a three-language wiki that a newcomer can follow without help.
- A repository whose description and topics make it findable.

### Intangible Benefits

- Practice in applying the course topics (APIs, typing, OOP, GUI) with professional review discipline.
- A reusable pattern for the other Day-NNN repositories of the course.

## Strategic Alignment

The project supports S01's goal of completing the bootcamp with portfolio-quality results, and the course repository group's goal of consistent, reviewable projects built on one framework.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC1 | Quiz runs end to end from the API | 10 questions answered, final score shown | Manual run recorded by the screenshot; unit tests of the API client with a fake response |
| SC2 | HTML entities removed | 0 occurrences of `&quot;`, `&#039;` and `&amp;` in displayed text | Unit test with an entity-laden fixture |
| SC3 | Answer checking | `true_pressed` and `false_pressed` give the same result as `check_answer` for 100 % of tested answers | Unit tests of the view model with a fake quiz |
| SC4 | Test suite | 100 % of tests pass; line coverage of the domain and application layers at least 90 % | `python -m pytest` output |
| SC5 | Setup from README | A fresh clone reaches a running app in 5 commands or fewer | Dry run of the README steps |
| SC6 | Runtime dependencies | 0 third-party runtime dependencies | `dependencies = []` in `pyproject.toml` |
| SC7 | Languages | Wiki has 3 languages with the same page set | Page listing and `framework/scripts/check-languages.sh` |
| SC8 | Traceability | 5 of 5 milestones `Accepted` with a `Go` review; every task closed by a pull request | Milestone documents and issue list |
| SC9 | The baseline milestone is done (O8) | The wiki sidebar has the framework's shape, `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` exit with code 0, 100 % of the continuous integration (CI) checks of the pull request of [MIL-005] pass | Files in `docs/wiki/`, the script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Open Trivia Database API is unavailable or rate-limits (HTTP 429) | The app cannot fetch questions | The API client raises a specific error, the interface shows a message, and the tests use a fake response |
| Tkinter is missing in a Python installation (some Linux distributions) | S02 cannot run the GUI | The README names the package to install; the domain and application layers run without it |
| Screenshots or commits expose a token | Disclosure of a secret | `.env` is git-ignored and never read by the application; screenshots show the application window only |
| Danish or Bahasa Malaysia text contains errors | S02 and S03 are misled | English is authoritative, translations follow it page by page, S01 is asked to check Danish, and Bahasa Malaysia is flagged as unchecked until a reader has checked it |
| The plan-first gate blocks work because a review is only a stand-in | Delay | The user's acceptance of the plan covers the language and domain check; the stand-in is recorded on each review |
| The documents of the baseline milestone [MIL-005] change documents that were accepted earlier, and the AI stand-in for S01 reviews them | Medium: a defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, the program and its tests are not changed, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 is Product Owner, developer and reviewer; the AI acts as stand-in author and reviewer in autonomous mode and says so on every record.
- The Open Trivia Database stays free and keyless; `amount=10&type=boolean` returns usable JSON.
- "Python greater than 3.13" is read as 3.13 or later (`requires-python = ">=3.13"`), because the installed interpreter is 3.13.
- The repository is the one named by `origin` (`Tirsvad-Udemy-100-days-of-code/034-quizzler` on `git.tirsystem.com`); the URL in the request (`Tirsvad-Udemy-100_days_of_code`) is taken as the organisation of that repository.
- The course images `true.png` and `false.png` from the starter archive may be reused for the buttons.

## Constraints

- Python 3.13 or later, `venv` for the environment, pytest for tests, `constants.py` for constants, `pyproject.toml` for configuration.
- Folder structure `src/`, `tests/`, `docs/`; Doxygen comments in the source and a `Doxyfile`.
- Tokens come from the git-ignored `.env`, for personal use only; the project neither imports nor tests it.
- One pull request per milestone; a reviewer other than the author merges (here: the user), and the AI never bypasses a required check.
- Target window: 2026-10-18 to 2026-10-25.
- The baseline milestone [MIL-005] starts 2026-11-16 and is finished within one week, by 2026-11-23. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.
- The Product Owner (PO) language is English and the PO domain is education (it was IT until [MIL-005]; the documents that [MIL-005] does not change keep the domain `it`, see the Open Issues of [PP-001]).

## Cost–Benefit Assessment

The assessment is qualitative: the project is a learning exercise with no revenue, and effort is the only cost, so a monetary ROI would be invented.

| Costs | Benefits |
| --- | --- |
| About 20 hours of S01's review time and about 4 hours of AI effort across four gateways | A published reference solution and a reusable repository pattern |
| No licence or hosting cost (public API, standard library, existing git host) | A findable repository for S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns, builds and reviews the result for the bootcamp (O1 to O7) |
| S02 | Needs readable, runnable code with the assignment's names and README instructions (O2, O3, O4, O5) |
| S03 | Needs a clear description, topics, README and no runtime dependencies (O5, O6) |

## Recommendation

Proceed — the scope is small, the risks have mitigations and every objective is verifiable by a milestone gate.

---

[SA-001]: ./stakeholder-analysis.md
[2133243]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/21332432e3c81336344ef3dbc71123aab76c9cfb
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[PP-001]: ./project-plan.md
[77b48ec]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/77b48ec969dadb9cee7c36ca091ee3977a06f030
