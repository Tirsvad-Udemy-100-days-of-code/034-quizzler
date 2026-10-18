# Quiz interface

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether a player can run the application, see a question from the API, answer it with the true or false button and see the result and the score.

## Deliverable

A pull request with the Tkinter `QuizInterface`, the `QuizViewModel`, the button images, the entry point `main.py` as composition root, and tests of the view model.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m quizzler` opens a window with a score label, a canvas with the question text and a true and a false image button | Window shown with all four elements | Any missing |
| 2 | The question text comes from `get_next_question`, which asks the quiz logic for the next question | Visible in the screenshot and in a view-model test | Fails |
| 3 | `true_pressed` and `false_pressed` are assigned to the buttons without parentheses and call `check_answer` with `"True"` and `"False"` | Test with a fake quiz records the two calls | Test fails |
| 4 | The player sees whether the answer was right or wrong and the score updates | Test of the view model passes; manual run confirms | Test fails |
| 5 | After the last question the buttons are disabled and the final score is shown | Test passes | Test fails |
| 6 | An API failure shows a readable message in the window and the process does not crash | Test with a failing fake source passes | Test fails |
| 7 | `python -m pytest` passes and Python code has a `Go` review record against `QC-PY-001` | Both hold | Either fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Needs `QuizBrain`, `Question` and the question source |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O3, O4 | [BC-001] |
| SC1, SC3, SC4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-23 — within the Business Case window of 2026-10-18 to 2026-10-25.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Build QuizInterface layout | Create the `QuizInterface` class with a Tkinter window, a score label, a canvas (300 x 250, white) for the question and two image buttons using the course's `true.png` and `false.png`, with padding and the theme colour from `constants.py`, as the "class-based GUI" lecture describes. | No | ADR-0001 |
| 2 | Add QuizViewModel and get_next_question | Add the view model that takes a `QuizBrain` (with a type hint), exposes `get_next_question`, the current text, the score and the finished state, and fits the question text to the canvas width. | No | ADR-0001 |
| 3 | Wire true_pressed and false_pressed | Add `true_pressed` and `false_pressed`, assigned to the buttons without parentheses so they run only on click, each calling `check_answer` with the corresponding value, as the "Check the Answer" lecture describes. | No | ADR-0001 |
| 4 | Show answer feedback and score | Show right or wrong feedback in the window (canvas colour flash) and update the score label, then move to the next question after a short delay, so the player does not depend on the console. | No | ADR-0001 |
| 5 | Handle end of quiz and API errors | Disable the buttons and show the final score after the last question, and show a readable message when the question source fails. | No | ADR-0001 |
| 6 | Add entry point and view-model tests | Add `main.py` and `python -m quizzler` as composition root, and pytest tests of the view model with fake quiz and fake source objects, without opening a window. | No | ADR-0001 |

---

[BC-001]: ../business-case.md
