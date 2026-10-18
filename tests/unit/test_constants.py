from quizzler import constants


def test_answers_are_true_and_false_strings() -> None:
    assert constants.TRUE_ANSWER == "True"
    assert constants.FALSE_ANSWER == "False"


def test_question_amount_is_positive() -> None:
    assert constants.QUESTION_AMOUNT > 0


def test_request_timeout_is_positive() -> None:
    assert constants.REQUEST_TIMEOUT_SECONDS > 0


def test_image_names_end_with_png() -> None:
    assert constants.TRUE_IMAGE_NAME.endswith(".png")
    assert constants.FALSE_IMAGE_NAME.endswith(".png")


def test_api_url_uses_https() -> None:
    assert constants.API_URL.startswith("https://")
