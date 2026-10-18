import time
import tkinter
from collections.abc import Iterator

import pytest

from quizzler.constants import THEME_COLOR
from quizzler.domain.question import Question
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.presentation.quiz_interface import QuizInterface

_CREATE_ATTEMPTS = 5
_RETRY_DELAY_SECONDS = 0.1


def _text_color(interface: QuizInterface) -> str:
    options = interface.canvas.itemconfig(interface.question_text)
    assert options is not None
    return str(options["fill"][-1])


def _create_interface(quiz: QuizBrain) -> QuizInterface:
    """Create the window, retrying the sporadic Tk start-up errors on Windows."""
    for attempt in range(_CREATE_ATTEMPTS):
        try:
            return QuizInterface(quiz)
        except tkinter.TclError as err:
            last_error = err
            time.sleep(_RETRY_DELAY_SECONDS * (attempt + 1))
    pytest.skip(f"no display available: {last_error}")


@pytest.fixture
def interface() -> Iterator[QuizInterface]:
    quiz = QuizBrain([Question("one", "True"), Question("two", "False")])
    created = _create_interface(quiz)
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


def test_buttons_are_disabled_during_feedback_and_enabled_after(
    interface: QuizInterface,
) -> None:
    interface.true_pressed()

    assert str(interface.true_button.cget("state")) == "disabled"
    assert str(interface.false_button.cget("state")) == "disabled"
    assert _text_color(interface) == "white"

    interface.get_next_question()

    assert str(interface.true_button.cget("state")) == "normal"
    assert str(interface.false_button.cget("state")) == "normal"
    assert _text_color(interface) == THEME_COLOR
