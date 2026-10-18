🌐 **English** · [Dansk](Architecture-da) · [Bahasa Melayu](Architecture-ms)

# Architecture

The code is split in layers; dependencies point inward (presentation to application to domain). The decision is recorded in ADR-0001 (`docs/adr/`).

| Folder | Holds |
| --- | --- |
| `src/quizzler/domain/` | `Question`, `QuizBrain` |
| `src/quizzler/application/` | `QuestionSource`, `build_question_bank` |
| `src/quizzler/infrastructure/` | `OpenTriviaClient` |
| `src/quizzler/presentation/` | `QuizInterface`, `QuizViewModel` |
| `src/quizzler/constants.py` | constants |
| `src/quizzler/main.py` | composition root |

## Course files and where they went

| Course file | Quizzler |
| --- | --- |
| `question_model.py` | `domain/question.py` |
| `quiz_brain.py` | `domain/quiz_brain.py` |
| `data.py` (`question_data`) | `infrastructure/open_trivia_client.py` + `application/build_question_bank.py` |
| `ui.py` | `presentation/quiz_interface.py`, `presentation/quiz_view_model.py` |
| `main.py` | `main.py` |

## Flow

`main()` asks `OpenTriviaClient` for ten records, `build_question_bank` turns them into `Question` objects (unescaping HTML entities such as `&quot;`), `QuizBrain` runs the quiz, and `QuizInterface` shows it. The buttons call `true_pressed` and `false_pressed`, which call `check_answer` with `"True"` or `"False"`.
