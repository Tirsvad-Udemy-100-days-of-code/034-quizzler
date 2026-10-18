"""Use case: turn the records of a question source into questions."""

from html import unescape

from quizzler.application.errors import QuestionSourceError
from quizzler.application.question_source import QuestionSource
from quizzler.constants import QUESTION_AMOUNT
from quizzler.domain.question import Question

_QUESTION_KEY = "question"
_ANSWER_KEY = "correct_answer"


def build_question_bank(
    source: QuestionSource, amount: int = QUESTION_AMOUNT
) -> list[Question]:
    """@brief Fetch records and map them to questions with plain text.

    HTML entities in the question and the answer are unescaped.

    @param source The port that supplies the raw records.
    @param amount How many questions to request.
    @return The questions, in the order the source returned them.
    @throws QuestionSourceError When the source fails or a record lacks a key.
    """
    questions: list[Question] = []
    for record in source.fetch_questions(amount):
        try:
            text = record[_QUESTION_KEY]
            answer = record[_ANSWER_KEY]
        except KeyError as err:
            raise QuestionSourceError(f"Record misses the key {err}.") from err
        questions.append(Question(text=unescape(text), answer=unescape(answer)))
    return questions
