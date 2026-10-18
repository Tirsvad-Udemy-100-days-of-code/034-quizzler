"""View model of the quiz screen; holds no widget and no tkinter import."""

from quizzler.constants import (
    FALSE_ANSWER,
    FINISHED_TEXT,
    SCORE_LABEL_PREFIX,
    TRUE_ANSWER,
)
from quizzler.domain.quiz_brain import QuizBrain


class QuizViewModel:
    """@brief Exposes the quiz to the view as text and commands."""

    def __init__(self, quiz: QuizBrain) -> None:
        """@brief Create a view model over a quiz.

        @param quiz The quiz whose state is shown.
        """
        self._quiz: QuizBrain = quiz
        self._is_finished: bool = False

    @property
    def score_text(self) -> str:
        """@brief The score label text, for example "Score: 3"."""
        return f"{SCORE_LABEL_PREFIX}{self._quiz.score}"

    @property
    def is_finished(self) -> bool:
        """@brief True once the last question has been passed."""
        return self._is_finished

    def get_next_question(self) -> str:
        """@brief Give the text to show next.

        @return The next question, or the finished text with the final score
            when no question is left.
        """
        if self._quiz.still_has_questions():
            return self._quiz.next_question()
        self._is_finished = True
        return f"{FINISHED_TEXT}\n{self.score_text}"

    def answer_true(self) -> bool:
        """@brief Answer the current question with "True".

        @return True when the answer is right.
        """
        return self._quiz.check_answer(TRUE_ANSWER)

    def answer_false(self) -> bool:
        """@brief Answer the current question with "False".

        @return True when the answer is right.
        """
        return self._quiz.check_answer(FALSE_ANSWER)
