"""The port through which the application obtains raw questions."""

from collections.abc import Mapping, Sequence
from typing import Protocol


class QuestionSource(Protocol):
    """@brief Supplies raw question records, wherever they come from."""

    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        """@brief Fetch question records.

        @param amount How many questions to fetch.
        @return Records with at least the keys "question" and "correct_answer".
        @throws QuestionSourceError When the questions cannot be obtained.
        """
        ...
