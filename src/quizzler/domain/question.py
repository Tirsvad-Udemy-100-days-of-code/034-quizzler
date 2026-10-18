"""The question entity."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Question:
    """@brief A true/false question with its correct answer.

    @param text The question as shown to the player.
    @param answer The correct answer, "True" or "False".
    """

    text: str
    answer: str
