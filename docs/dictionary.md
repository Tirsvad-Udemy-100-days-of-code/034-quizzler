# Domain Dictionary: Quizzler

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [2133243] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term for Quizzler. The PO language is English (`en`) and the PO domain is Software and IT (`it`); the PO terms are the words of the course assignment and of S01, the IT terms are the class, method and attribute names used in the source code. The dictionary covers the terms of [BC-001]; the project has no Domain Model yet.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| quiz question | en | Question | A statement that the player judges to be true or false. | BC, MIL | PY |
| question text | en | text | The sentence of a quiz question as shown to the player. | BC, MIL | PY |
| correct answer | en | answer | The value, True or False, that the trivia source gives for a quiz question. | BC, MIL | PY |
| quiz round | en | QuizBrain | The logic that steps through the quiz questions, checks answers and keeps the score. | BC, MIL | PY |
| question bank | en | question_list | The ordered collection of quiz questions for one round. | BC, MIL | PY |
| trivia source | en | question_source | The service that supplies quiz questions, here the Open Trivia Database. | BC, MIL | PY |
| score | en | score | The number of correct answers given in the current round. | BC, MIL | PY |
| quiz window | en | QuizInterface | The Tkinter window in which the player sees questions and answers. | BC, MIL | PY |
| answer button | en | true_pressed, false_pressed | The True or False button whose click hands the player's answer to the quiz round. | BC, MIL | PY |
| answer check | en | check_answer | The comparison of the player's answer with the correct answer. | BC, MIL | PY |
| HTML entity | en | escaped character | A character written as a code such as `&quot;` that must be unescaped before display. | BC, MIL | PY |

## Rules

- The Business Case and the milestones use the PO term; the source code uses the IT term. `PY` is the short name of Python source code in the catalog.
- One IT term per PO term and one PO term per IT term; no synonyms.
- A new concept in the code gets a row in the same change.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[2133243]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/21332432e3c81336344ef3dbc71123aab76c9cfb
