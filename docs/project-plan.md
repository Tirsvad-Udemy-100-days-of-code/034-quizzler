# Project Plan: Quizzler

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version, accepted by the Product Owner with the plan | [2133243] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added the baseline gateway (MIL-005) with its schedule row, scope coverage, dependency, risk and Gantt entries; linked the first four gateways to their milestones on the git host; set the domain to education; reviewed in autonomous mode, not independent | [77b48ec] |

---

## Purpose

Schedules the four gateways that deliver Quizzler within the Business Case window of 2026-10-18 to 2026-10-25 ([BC-001]), and the baseline gateway ([MIL-005]) that was added later. Each gateway is one milestone document, one Milestone on the git host and one pull request.

## Planning Assumptions

- Week 1 starts 2026-10-18; the plan ends by 2026-10-25, per the Business Case constraint.
- The baseline gateway ([MIL-005]) starts 2026-11-16 and ends 2026-11-23, one week, as the Business Case constraint for it requires. It brings the finished project to the baseline of the framework (decision of S01); the first four gateways keep their dates.
- Phase length: two days per gateway. S01 is the only owner and reviewer ([SA-001]); the AI acts as stand-in author and reviewer in autonomous mode.
- The baseline (Business Case, Stakeholder Analysis, Project Plan, governance, dictionary, ADR-0001, milestones) is accepted when the user accepts this plan in chat; MIL-001 starts after that.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project foundation | [MIL-001] | 2026-10-18 to 2026-10-19 | 2026-10-19 | S01 | none | Configuration, skeleton, README, repository description and topics | [Milestone 198][M-198] |
| Quiz core | [MIL-002] | 2026-10-20 to 2026-10-21 | 2026-10-21 | S01 | none | Question model, quiz logic, API client, tests | [Milestone 199][M-199] |
| Quiz interface | [MIL-003] | 2026-10-22 to 2026-10-23 | 2026-10-23 | S01 | none | Tkinter interface, answer checking, entry point | [Milestone 200][M-200] |
| Documentation and wiki | [MIL-004] | 2026-10-24 to 2026-10-25 | 2026-10-25 | S01 | none | Screenshots, README, wiki in three languages | [Milestone 201][M-201] |
| Framework baseline | [MIL-005] | 2026-11-16 to 2026-11-23 | 2026-11-23 | S01 | none | The adopted framework release, the wiki sidebar in the framework's shape, the README, licence metadata, the traceability matrix and review records | [Milestone 549][M-549] |

```plantuml
@startgantt
Project starts 2026-10-18
[Project foundation] starts 2026-10-18 and ends 2026-10-19
[Quiz core] starts 2026-10-20 and ends 2026-10-21
[Quiz interface] starts 2026-10-22 and ends 2026-10-23
[Documentation and wiki] starts 2026-10-24 and ends 2026-10-25
[Foundation Go/No-Go] happens 2026-10-19
[Core Go/No-Go] happens 2026-10-21
[Interface Go/No-Go] happens 2026-10-23
[Documentation Go/No-Go] happens 2026-10-25
[Framework baseline] starts 2026-11-16 and ends 2026-11-23
[Baseline Go/No-Go] happens 2026-11-23
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Question model, quiz logic, API client | MIL-002 |
| Answer checking and Tkinter interface, entry point | MIL-003 |
| Project configuration, folder structure, `constants.py`, `Doxyfile` | MIL-001 |
| pytest tests | MIL-001 (set-up), MIL-002 and MIL-003 (tests) |
| README with run and test instructions | MIL-001 (first version), MIL-004 (finished) |
| Screenshot, wiki in three languages | MIL-004 |
| Repository description and topics | MIL-001 |
| The baseline: framework release, wiki sidebar, README, licence metadata, traceability matrix, review records | [MIL-005] |

## Dependencies

```
MIL-001 → MIL-002 → MIL-003 → MIL-004 → MIL-005
```

A No-Go on a gateway stops the chain: later windows move by the days needed to fix it, and the Business Case window is renegotiated with S01 if it runs past 2026-10-25. S01 decides the new dates. A No-Go on [MIL-005] leaves the program and the earlier gateways as they are.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The git host API or token fails when setting description and topics | MIL-001 cannot close criterion 6 | The tool stops and reports; S01 sets them by hand in the web UI |
| A required CI check on the host fails for a reason outside the project | A pull request cannot merge | Stop after three attempts on the same cause and report, as AGENTS.md requires |
| Screenshots need a desktop session | MIL-004 delay | Capture on S01's own Windows desktop with the application window only |
| A continuous integration (CI) check fails on the pull request of [MIL-005] | The merge is delayed past 2026-11-23 | The failure is fixed on the same branch and the checks run again; after three failed rounds on one cause the work stops and S01 decides (trace: SC9 of [BC-001]) |

## Open Issues

- The repository URL in the request (`Tirsvad-Udemy-100_days_of_code`) differs from `origin` (`Tirsvad-Udemy-100-days-of-code/034-quizzler`); the plan uses `origin`.
- Bahasa Malaysia text cannot be checked by S01 or the AI as a reader of the language; it stays flagged as unchecked in the wiki.
- The plan was accepted without a QC checklist until [MIL-005]; since then it is reviewed against `QC-PP-001` ([RC-015]).
- Domain: since [MIL-005] the plan, the Business Case, the Traceability Matrix and the baseline milestone have the domain `education`. The other documents (Stakeholder Analysis, Domain Dictionary, Governance, milestones MIL-001 to MIL-004 and the review records RC-001 to RC-013) keep the domain `it` they were accepted with; they are not changed by the baseline, and a change of their domain would need a new review of each. The Domain Dictionary still names `it` as the PO domain in its Purpose and Scope.
- The wiki publishing workflow that MIL-004 added (its task 6, issue 25) was removed in the commit "Use git-workflows and the scoped workflows" (pull request #33), because the shared workflows of the git host publish `docs/wiki/`; the task stays in MIL-004 as the accepted record.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-project-foundation.md
[MIL-002]: ./milestones/mil-002-quiz-core.md
[MIL-003]: ./milestones/mil-003-quiz-interface.md
[MIL-004]: ./milestones/mil-004-documentation-and-wiki.md
[2133243]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/21332432e3c81336344ef3dbc71123aab76c9cfb
[M-198]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/milestones/198
[M-199]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/milestones/199
[M-200]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/milestones/200
[M-201]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/milestones/201
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[RC-015]: ./sqa/reviews/rc-015-project-plan-baseline.md
[M-549]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/milestones/549
[77b48ec]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/commit/77b48ec969dadb9cee7c36ca091ee3977a06f030
