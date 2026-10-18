🌐 [English](Architecture) · **Dansk** · [Bahasa Melayu](Architecture-ms)

# Arkitektur

Koden er delt i lag; afhængigheder peger indad (presentation til application til domain). Beslutningen er beskrevet i ADR-0001 (`docs/adr/`).

| Mappe | Indeholder |
| --- | --- |
| `src/quizzler/domain/` | `Question`, `QuizBrain` |
| `src/quizzler/application/` | `QuestionSource`, `build_question_bank` |
| `src/quizzler/infrastructure/` | `OpenTriviaClient` |
| `src/quizzler/presentation/` | `QuizInterface`, `QuizViewModel` |
| `src/quizzler/constants.py` | constants |
| `src/quizzler/main.py` | composition root |

## Kursets filer og hvor de blev af

| Kursusfil | Quizzler |
| --- | --- |
| `question_model.py` | `domain/question.py` |
| `quiz_brain.py` | `domain/quiz_brain.py` |
| `data.py` (`question_data`) | `infrastructure/open_trivia_client.py` + `application/build_question_bank.py` |
| `ui.py` | `presentation/quiz_interface.py`, `presentation/quiz_view_model.py` |
| `main.py` | `main.py` |

## Forløb

`main()` beder `OpenTriviaClient` om ti poster, `build_question_bank` gør dem til `Question`-objekter (og afkoder HTML-entiteter som `&quot;`), `QuizBrain` kører quizzen, og `QuizInterface` viser den. Knapperne kalder `true_pressed` og `false_pressed`, som kalder `check_answer` med `"True"` eller `"False"`.
