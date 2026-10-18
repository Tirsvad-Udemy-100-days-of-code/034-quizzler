import tkinter
from collections.abc import Iterator

import pytest

from quizzler.domain.question import Question
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.presentation.quiz_interface import QuizInterface


@pytest.fixture
def interface() -> Iterator[QuizInterface]:
    quiz = QuizBrain([Question("one", "True"), Question("two", "False")])
    try:
        created = QuizInterface(quiz)
    except tkinter.TclError:
        pytest.skip("no display available")
    yield created
    created.window.destroy()


def test_true_button_command_updates_score_when_answer_is_right(
    interface: QuizInterface,
) -> None:
    interface.true_button.invoke()

    assert interface.score_label.cget("text") == "Score: 1"


def test_false_button_command_keeps_score_when_answer_is_wrong(
    interface: QuizInterface,
) -> None:
    interface.false_button.invoke()

    assert interface.score_label.cget("text") == "Score: 0"
