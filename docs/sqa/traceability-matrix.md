# Traceability Matrix: Quizzler

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [DICT-001], [GOV-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-011 (Python source of MIL-002 (`domain`, `application`, `infrastructure`)) | [0f8ab48] |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-012 (Python source of MIL-003 (`presentation`, `main.py`)) | [7916603] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added MIL-005, the review records RC-014 to RC-017 and the wiki; set the reviewed rows of BC-001 and PP-001 and the domain of the changed rows to education (autonomous, not independent) | [77b48ec] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's cross-artifact traceability objective (O7) is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [DICT-001], [GOV-001], [ADR-0001], [MIL-005] | [RC-014], [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [GOV-001] | [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-015] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-003] |
| [GOV-001] | GOV | en | it | [BC-001], [SA-001] | [TM-001] | [RC-004] |
| [ADR-0001] | ADR | - | - | [BC-001] | source code under `src/` | [RC-005] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | source code, configuration and README | [RC-006] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | source code and tests of the domain, application and infrastructure layers | [RC-007] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | source code and tests of the presentation layer | [RC-008] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | README, screenshots and wiki, [MIL-005] | [RC-009] |
| [MIL-005] | MIL | en | education | [BC-001], [PP-001], [MIL-004] | - | [RC-016] |
| Python source of MIL-001 (`src/quizzler`, `tests`) | PY | - | - | [ADR-0001], [MIL-001] | - | [RC-010] |
| Python source of MIL-002 (`domain`, `application`, `infrastructure`) | PY | - | - | [ADR-0001], [MIL-002] | - | [RC-011] |
| Python source of MIL-003 (`presentation`, `main.py`) | PY | - | - | [ADR-0001], [MIL-003] | - | [RC-012] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-005] | - | [RC-017] |

## Coverage Notes

- No instance exists yet of KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD or ERD: the requirements come from the course assignment (see [BC-001]) and the design reference is [ADR-0001].
- [PP-001] was accepted without a QC checklist; it is reviewed against `QC-PP-001` for the first time in [RC-015].
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-017].
- The project workflow `.gitea/workflows/publish-wiki.yml` that MIL-004 added was removed in pull request #33, when the repository moved to the shared workflows of the git host; [RC-013] reviewed it while it existed. `.gitea/workflows/quality.yml` is still reviewed there.
- The domain of [BC-001], [PP-001], [MIL-005] and the wiki is `education` since [MIL-005]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-005] changes no source file, so the source code is not reviewed again.
- In Upstream `-` means foundational; in Downstream `-` means nothing is built on it yet; in Last Reviewed `-` means no `RC-*` exists.
- Source code is reviewed against `QC-PY-001` before each pull request; those records are added to this matrix as they are written.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[GOV-001]: ./governance.md
[ADR-0001]: ../adr/adr-0001-architecture-and-dependencies.md
[MIL-001]: ../milestones/mil-001-project-foundation.md
[MIL-002]: ../milestones/mil-002-quiz-core.md
[MIL-003]: ../milestones/mil-003-quiz-interface.md
[MIL-004]: ../milestones/mil-004-documentation-and-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-dictionary.md
[RC-004]: ./reviews/rc-004-governance.md
[RC-005]: ./reviews/rc-005-adr-0001.md
[RC-006]: ./reviews/rc-006-mil-001.md
[RC-007]: ./reviews/rc-007-mil-002.md
[RC-008]: ./reviews/rc-008-mil-003.md
[RC-009]: ./reviews/rc-009-mil-004.md
[RC-010]: ./reviews/rc-010-py-mil-001.md
[RC-011]: ./reviews/rc-011-py-mil-002.md
[0f8ab48]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/0f8ab48feaaf83deb905fc58edad911dc9a619d2
[RC-012]: ./reviews/rc-012-py-mil-003.md
[7916603]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/79166039748a84d15538bd57c6633ccecfe53921
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-014]: ./reviews/rc-014-business-case-baseline.md
[RC-015]: ./reviews/rc-015-project-plan-baseline.md
[RC-016]: ./reviews/rc-016-milestone-005.md
[RC-017]: ./reviews/rc-017-wiki.md
[TM-001]: ./traceability-matrix.md
[RC-013]: ./reviews/rc-013-ci-workflows.md
[77b48ec]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/77b48ec969dadb9cee7c36ca091ee3977a06f030
