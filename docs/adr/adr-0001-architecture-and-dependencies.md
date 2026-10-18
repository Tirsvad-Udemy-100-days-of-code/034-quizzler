# ADR-0001: Architecture and dependencies

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The course starter code is five flat files (`main.py`, `question_model.py`, `quiz_brain.py`, `data.py`, `ui.py`). The Business Case ([BC-001]) asks for readable code that keeps the assignment's names (S02), no runtime dependencies (S03, success criterion SC6), tests that need no network (SC4) and the folder structure `src/`, `tests/`, `docs/`. The coding conventions require the Clean Architecture layers `domain`, `application`, `infrastructure` and `presentation`, and the presentation pattern MVVM for a user interface. The project has no use-case or class-diagram artifacts: the design source is the course assignment, and this record is the design reference that the code is reviewed against.

Options for the layout:

1. Keep the five flat files, as in the course. Simple, but not testable without Tkinter and the network, and it fails the layering criterion of the Python checklist.
2. Layers under `src/quizzler/` with the assignment's class and method names kept inside them.

Options for the HTTP client:

1. `requests`. Convenient, but a runtime dependency.
2. `urllib.request` and `json` from the standard library. A few more lines, no dependency.

## Decision

We use option 2 for the layout: `domain` holds `Question` and `QuizBrain` (with `still_has_questions`, `next_question`, `check_answer`), `application` holds the `QuestionSource` port and the use case that builds the question bank, `infrastructure` holds the Open Trivia Database client (standard library `urllib.request`, `html.unescape`), and `presentation` holds the Tkinter `QuizInterface` as the view and a `QuizViewModel` that owns the interface state; `main.py` is the composition root. We use `urllib.request` rather than `requests`, so the runtime `dependencies` list stays empty, and all constants live in `src/quizzler/constants.py`.

`check_answer` receives the answer as the strings `"True"` or `"False"` (constants `TRUE_ANSWER` and `FALSE_ANSWER`), as in the course, and `true_pressed` and `false_pressed` pass those values.

## Consequences

**Positive:**

- The domain and application layers are tested without Tkinter or the network, using a fake `QuestionSource`.
- No third-party runtime dependency to install or trust.
- The assignment's names remain recognisable to S02.

**Negative:**

- More files than the course has; the README maps the course files to the layers.
- Hand-written HTTP error handling instead of the `requests` conveniences.
- The Tkinter view itself is covered by the view model's tests and a manual run, not by automated GUI tests.

Quality-attribute impacts: portability improves (standard library only), maintainability improves (inward dependencies), performance is unaffected for ten questions.

## Affected Artifacts

- [BC-001] — objectives O1 to O5 and success criteria SC4 and SC6 are met by this layout.

---

[BC-001]: ../business-case.md
