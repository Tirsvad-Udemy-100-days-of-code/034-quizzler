"""Composition root: wires the question source, the quiz and the window."""

from collections.abc import Callable

from quizzler.application.build_question_bank import build_question_bank
from quizzler.application.errors import QuestionSourceError
from quizzler.application.question_source import QuestionSource
from quizzler.constants import ERROR_TEXT
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.infrastructure.open_trivia_client import OpenTriviaClient

_EXIT_OK = 0
_EXIT_FAILURE = 1


def _show_quiz(quiz: QuizBrain) -> None:
    """@brief Open the quiz window and run it.

    tkinter is imported here so that importing this module stays headless.

    @param quiz The quiz to play.
    """
    from quizzler.presentation.quiz_interface import QuizInterface

    QuizInterface(quiz).run()


def _show_error(message: str) -> None:
    """@brief Open the error window.

    tkinter is imported here so that importing this module stays headless.

    @param message The text to show.
    """
    from quizzler.presentation.quiz_interface import show_error

    show_error(message)


def main(
    source: QuestionSource | None = None,
    show_quiz: Callable[[QuizBrain], None] = _show_quiz,
    show_error: Callable[[str], None] = _show_error,
) -> int:
    """@brief Run the application.

    @param source Where the questions come from; the Open Trivia client if None.
    @param show_quiz Shows the quiz to the player.
    @param show_error Shows an error message to the player.
    @return 0 on success, 1 when the questions could not be loaded.
    """
    question_source = source if source is not None else OpenTriviaClient()
    try:
        questions = build_question_bank(question_source)
    except QuestionSourceError as err:
        show_error(f"{ERROR_TEXT}\n{err}")
        return _EXIT_FAILURE
    show_quiz(QuizBrain(questions))
    return _EXIT_OK
