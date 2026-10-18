import dataclasses

import pytest

from quizzler.domain.question import Question


def test_question_keeps_text_and_answer() -> None:
    question = Question(text="Is water wet?", answer="True")

    assert question.text == "Is water wet?"
    assert question.answer == "True"


def test_question_is_immutable() -> None:
    question = Question(text="Is water wet?", answer="True")

    with pytest.raises(dataclasses.FrozenInstanceError):
        question.text = "other"  # type: ignore[misc]


def test_questions_with_same_values_are_equal() -> None:
    assert Question("a", "True") == Question("a", "True")
