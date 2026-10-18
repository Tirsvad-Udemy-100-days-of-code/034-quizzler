import pytest

from quizzler.constants import FALSE_ANSWER, TRUE_ANSWER
from quizzler.domain.errors import NoCurrentQuestionError, QuizFinishedError
from quizzler.domain.question import Question
from quizzler.domain.quiz_brain import QuizBrain


@pytest.fixture
def brain() -> QuizBrain:
    return QuizBrain(
        [
            Question("First?", TRUE_ANSWER),
            Question("Second?", FALSE_ANSWER),
        ]
    )


def test_new_quiz_starts_with_zero_score_and_number(brain: QuizBrain) -> None:
    assert brain.score == 0
    assert brain.question_number == 0
    assert brain.current_question is None


def test_still_has_questions_is_true_at_start(brain: QuizBrain) -> None:
    assert brain.still_has_questions()


def test_still_has_questions_is_false_for_empty_list() -> None:
    assert not QuizBrain([]).still_has_questions()


def test_next_question_returns_numbered_text(brain: QuizBrain) -> None:
    assert brain.next_question() == "Q.1: First?"
    assert brain.next_question() == "Q.2: Second?"
    assert brain.question_number == 2
    assert brain.current_question == Question("Second?", FALSE_ANSWER)


def test_still_has_questions_is_false_after_last(brain: QuizBrain) -> None:
    brain.next_question()
    brain.next_question()

    assert not brain.still_has_questions()


def test_next_question_raises_when_none_left(brain: QuizBrain) -> None:
    brain.next_question()
    brain.next_question()

    with pytest.raises(QuizFinishedError):
        brain.next_question()


def test_check_answer_scores_correct_answer(brain: QuizBrain) -> None:
    brain.next_question()

    assert brain.check_answer(TRUE_ANSWER)
    assert brain.score == 1


def test_check_answer_ignores_case(brain: QuizBrain) -> None:
    brain.next_question()

    assert brain.check_answer("tRuE")
    assert brain.score == 1


def test_check_answer_does_not_score_wrong_answer(brain: QuizBrain) -> None:
    brain.next_question()

    assert not brain.check_answer(FALSE_ANSWER)
    assert brain.score == 0


def test_check_answer_raises_before_first_question(brain: QuizBrain) -> None:
    with pytest.raises(NoCurrentQuestionError):
        brain.check_answer(TRUE_ANSWER)
