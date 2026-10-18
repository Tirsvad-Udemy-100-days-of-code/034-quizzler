from collections.abc import Mapping, Sequence

from quizzler.application.errors import QuestionSourceError
from quizzler.constants import ERROR_TEXT
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.main import main


class FakeQuestionSource:
    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        return [
            {"question": "one", "correct_answer": "True"},
            {"question": "two", "correct_answer": "False"},
        ]


class FailingQuestionSource:
    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        raise QuestionSourceError("offline")


def test_main_shows_error_and_returns_one_when_source_fails() -> None:
    quizzes: list[QuizBrain] = []
    messages: list[str] = []

    code = main(FailingQuestionSource(), quizzes.append, messages.append)

    assert code == 1
    assert quizzes == []
    assert len(messages) == 1
    assert ERROR_TEXT in messages[0]
    assert "offline" in messages[0]


def test_main_shows_quiz_and_returns_zero_when_source_works() -> None:
    quizzes: list[QuizBrain] = []
    messages: list[str] = []

    code = main(FakeQuestionSource(), quizzes.append, messages.append)

    assert code == 0
    assert messages == []
    assert len(quizzes) == 1
    assert len(quizzes[0].question_list) == 2
