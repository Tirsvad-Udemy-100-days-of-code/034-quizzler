"""The quiz rules: asking questions in order and keeping the score."""

from quizzler.domain.errors import NoCurrentQuestionError, QuizFinishedError
from quizzler.domain.question import Question


class QuizBrain:
    """@brief Runs a quiz over a list of questions and keeps the score."""

    def __init__(self, question_list: list[Question]) -> None:
        """@brief Create a quiz at its start.

        @param question_list The questions, asked in list order.
        """
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list[Question] = question_list
        self.current_question: Question | None = None

    def still_has_questions(self) -> bool:
        """@brief Tell whether another question can be asked.

        @return True when at least one question has not been asked yet.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """@brief Advance to the next question.

        @return The numbered question text, for example "Q.1: Is the sky blue?".
        @throws QuizFinishedError When no question is left.
        """
        if not self.still_has_questions():
            raise QuizFinishedError("There are no questions left.")
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer: str) -> bool:
        """@brief Compare an answer with the current question, ignoring case.

        The score goes up by one when the answer is right.

        @param user_answer The answer given by the player.
        @return True when the answer is correct.
        @throws NoCurrentQuestionError When no question has been asked yet.
        """
        if self.current_question is None:
            raise NoCurrentQuestionError("No question has been asked yet.")
        is_correct = user_answer.lower() == self.current_question.answer.lower()
        if is_correct:
            self.score += 1
        return is_correct
