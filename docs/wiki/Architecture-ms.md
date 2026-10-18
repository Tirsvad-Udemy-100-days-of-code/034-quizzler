🌐 [English](Architecture) · [Dansk](Architecture-da) · **Bahasa Melayu**

# Seni bina

> Nota: terjemahan Bahasa Melayu ini belum disemak oleh penutur asli; bahasa Inggeris ialah teks rasmi.

Kod dibahagi kepada lapisan; kebergantungan menghala ke dalam (presentation ke application ke domain). Keputusan ini direkodkan dalam ADR-0001 (`docs/adr/`).

| Folder | Mengandungi |
| --- | --- |
| `src/quizzler/domain/` | `Question`, `QuizBrain` |
| `src/quizzler/application/` | `QuestionSource`, `build_question_bank` |
| `src/quizzler/infrastructure/` | `OpenTriviaClient` |
| `src/quizzler/presentation/` | `QuizInterface`, `QuizViewModel` |
| `src/quizzler/constants.py` | constants |
| `src/quizzler/main.py` | composition root |

## Fail kursus dan di mana ia berada sekarang

| Fail kursus | Quizzler |
| --- | --- |
| `question_model.py` | `domain/question.py` |
| `quiz_brain.py` | `domain/quiz_brain.py` |
| `data.py` (`question_data`) | `infrastructure/open_trivia_client.py` + `application/build_question_bank.py` |
| `ui.py` | `presentation/quiz_interface.py`, `presentation/quiz_view_model.py` |
| `main.py` | `main.py` |

## Aliran

`main()` meminta sepuluh rekod daripada `OpenTriviaClient`, `build_question_bank` menukarnya kepada objek `Question` (dan menyahkod entiti HTML seperti `&quot;`), `QuizBrain` menjalankan kuiz, dan `QuizInterface` memaparkannya. Butang memanggil `true_pressed` dan `false_pressed`, yang memanggil `check_answer` dengan `"True"` atau `"False"`.
