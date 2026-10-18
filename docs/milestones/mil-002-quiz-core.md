# Quiz core

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [2133243] |

---

## Purpose

Decides whether the quiz logic and the question source work and are tested without Tkinter and without the network, so the interface gateway can build on them.

## Deliverable

A pull request with the domain and application layers (`Question`, `QuizBrain`, `QuestionSource`, the question-bank use case), the Open Trivia Database client, and their pytest tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `QuizBrain` offers `still_has_questions`, `next_question` and `check_answer` and keeps the score | Present and tested | Any missing |
| 2 | The client requests `amount=10&type=boolean` and returns `Question` objects | Test with a fake response passes | Test fails |
| 3 | HTML entities in question text are unescaped | Fixture with `&quot;` and `&#039;` yields plain text | Entities remain |
| 4 | An unreachable API or an API error response raises a specific error | Tests for network failure and non-zero response code pass | Test fails |
| 5 | `python -m pytest` passes without network access and line coverage of `domain` and `application` is at least 90 % | Both hold | Either fails |
| 6 | Python code has a `Go` review record against `QC-PY-001` | `Go` | Anything else |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs `pyproject.toml`, the package skeleton, `constants.py` and the pytest set-up |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O4 | [BC-001] |
| SC1, SC2, SC4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — within the Business Case window of 2026-10-18 to 2026-10-25.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement Question model | Add the immutable `Question` with `text` and `answer`, as in the course's `question_model.py`, in the domain layer, with Doxygen comments and tests. | No | ADR-0001 |
| 2 | Implement QuizBrain | Add `QuizBrain` with `still_has_questions`, `next_question` (returns the next question text with its number) and `check_answer` (compares the "True"/"False" answer case-insensitively and updates the score), as the course's lectures describe. No `input()` or `print` in the domain layer. | No | ADR-0001 |
| 3 | Add QuestionSource port and question-bank use case | Define the `QuestionSource` protocol and the use case that turns the source's data into `Question` objects, so the domain does not know the API. | No | ADR-0001 |
| 4 | Implement Open Trivia Database client | Build the request URL with the parameters `amount` and `type=boolean` from `constants.py`, fetch it with `urllib.request`, parse the JSON, and raise a specific error on network failure, a non-zero `response_code` or invalid JSON. | No | ADR-0001 |
| 5 | Unescape HTML entities | Apply `html.unescape` to each question text so that text such as `&quot;Mario Kart 64&quot;` is shown as readable text, as the "Unescaping HTML Entities" lecture teaches. | No | ADR-0001 |
| 6 | Add unit tests for the core | Write pytest tests for `Question`, `QuizBrain`, the use case and the client using a fake source and a fake HTTP response, with no network access. | No | ADR-0001 |

---

[BC-001]: ../business-case.md
[2133243]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/21332432e3c81336344ef3dbc71123aab76c9cfb
