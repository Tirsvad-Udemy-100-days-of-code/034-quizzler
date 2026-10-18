from quizzler.constants import FALSE_ANSWER, FINISHED_TEXT, TRUE_ANSWER
from quizzler.domain.question import Question
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.presentation.quiz_view_model import QuizViewModel


class RecordingQuizBrain(QuizBrain):
    def __init__(self, question_list: list[Question]) -> None:
        super().__init__(question_list)
        self.answers: list[str] = []

    def check_answer(self, user_answer: str) -> bool:
        self.answers.append(user_answer)
        return super().check_answer(user_answer)


def _view_model(*answers: str) -> tuple[QuizViewModel, RecordingQuizBrain]:
    quiz = RecordingQuizBrain([Question(f"q{i}", a) for i, a in enumerate(answers)])
    return QuizViewModel(quiz), quiz


def test_get_next_question_returns_numbered_text() -> None:
    view_model, _ = _view_model(TRUE_ANSWER)

    assert view_model.get_next_question() == "Q.1: q0"


def test_answer_true_checks_true_answer() -> None:
    view_model, quiz = _view_model(TRUE_ANSWER)
    view_model.get_next_question()

    view_model.answer_true()

    assert quiz.answers == [TRUE_ANSWER]


def test_answer_false_checks_false_answer() -> None:
    view_model, quiz = _view_model(TRUE_ANSWER)
    view_model.get_next_question()

    view_model.answer_false()

    assert quiz.answers == [FALSE_ANSWER]


def test_answer_true_returns_true_when_right() -> None:
    view_model, _ = _view_model(TRUE_ANSWER)
    view_model.get_next_question()

    assert view_model.answer_true() is True


def test_answer_true_returns_false_when_wrong() -> None:
    view_model, _ = _view_model(FALSE_ANSWER)
    view_model.get_next_question()

    assert view_model.answer_true() is False


def test_score_text_starts_at_zero() -> None:
    view_model, _ = _view_model(TRUE_ANSWER)

    assert view_model.score_text == "Score: 0"


def test_score_text_counts_right_answers_only() -> None:
    view_model, _ = _view_model(TRUE_ANSWER, TRUE_ANSWER)
    view_model.get_next_question()
    view_model.answer_true()
    view_model.get_next_question()
    view_model.answer_false()

    assert view_model.score_text == "Score: 1"


def test_is_finished_is_false_while_questions_remain() -> None:
    view_model, _ = _view_model(TRUE_ANSWER)
    view_model.get_next_question()

    assert view_model.is_finished is False


def test_get_next_question_returns_finished_text_with_score_at_end() -> None:
    view_model, _ = _view_model(TRUE_ANSWER)
    view_model.get_next_question()
    view_model.answer_true()

    text = view_model.get_next_question()

    assert text == f"{FINISHED_TEXT}\nScore: 1"
    assert view_model.is_finished is True
