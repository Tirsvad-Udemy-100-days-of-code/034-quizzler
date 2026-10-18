from collections.abc import Mapping, Sequence

import pytest

from quizzler.application.build_question_bank import build_question_bank
from quizzler.application.errors import QuestionSourceError
from quizzler.constants import QUESTION_AMOUNT
from quizzler.domain.question import Question


class FakeQuestionSource:
    def __init__(self, records: Sequence[Mapping[str, str]]) -> None:
        self._records = records
        self.requested_amount: int | None = None

    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        self.requested_amount = amount
        return self._records


class FailingQuestionSource:
    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        raise QuestionSourceError("down")


def test_build_question_bank_maps_records_to_questions() -> None:
    source = FakeQuestionSource([{"question": "Is it?", "correct_answer": "True"}])

    assert build_question_bank(source) == [Question("Is it?", "True")]


def test_build_question_bank_unescapes_html_entities() -> None:
    source = FakeQuestionSource(
        [
            {
                "question": "&quot;Mario Kart 64&quot; isn&#039;t Tom &amp; Jerry, "
                "caf&eacute;?",
                "correct_answer": "False",
            }
        ]
    )

    [question] = build_question_bank(source)

    assert question.text == '"Mario Kart 64" isn\'t Tom & Jerry, café?'


def test_build_question_bank_unescapes_answer() -> None:
    source = FakeQuestionSource([{"question": "q", "correct_answer": "&#84;rue"}])

    assert build_question_bank(source)[0].answer == "True"


def test_build_question_bank_requests_default_amount() -> None:
    source = FakeQuestionSource([])

    build_question_bank(source)

    assert source.requested_amount == QUESTION_AMOUNT


def test_build_question_bank_requests_given_amount() -> None:
    source = FakeQuestionSource([])

    build_question_bank(source, amount=3)

    assert source.requested_amount == 3


def test_build_question_bank_raises_on_missing_key() -> None:
    source = FakeQuestionSource([{"question": "no answer"}])

    with pytest.raises(QuestionSourceError):
        build_question_bank(source)


def test_build_question_bank_propagates_source_error() -> None:
    with pytest.raises(QuestionSourceError):
        build_question_bank(FailingQuestionSource())
