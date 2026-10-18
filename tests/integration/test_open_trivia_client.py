import io
import json
import urllib.error
from email.message import Message

import pytest

from quizzler.application.errors import QuestionSourceError
from quizzler.constants import REQUEST_TIMEOUT_SECONDS
from quizzler.infrastructure.open_trivia_client import OpenTriviaClient

RECORD = {"question": "Is it?", "correct_answer": "True"}


class FakeOpener:
    """Stands in for the network: records the call, returns or raises."""

    def __init__(self, body: bytes = b"", error: Exception | None = None) -> None:
        self._body = body
        self._error = error
        self.url: str | None = None
        self.timeout: float | None = None

    def __call__(self, url: str, timeout: float) -> bytes:
        self.url = url
        self.timeout = timeout
        if self._error is not None:
            raise self._error
        return self._body


def _body(response_code: int = 0) -> bytes:
    return json.dumps({"response_code": response_code, "results": [RECORD]}).encode()


def test_build_url_contains_amount_and_type() -> None:
    url = OpenTriviaClient().build_url(10)

    assert "amount=10" in url
    assert "type=boolean" in url


def test_fetch_questions_requests_url_with_timeout() -> None:
    opener = FakeOpener(_body())

    OpenTriviaClient(opener).fetch_questions(10)

    assert opener.url is not None
    assert "amount=10" in opener.url
    assert "type=boolean" in opener.url
    assert opener.timeout == REQUEST_TIMEOUT_SECONDS


def test_fetch_questions_returns_results() -> None:
    assert OpenTriviaClient(FakeOpener(_body())).fetch_questions(10) == [RECORD]


def test_fetch_questions_raises_on_network_failure() -> None:
    opener = FakeOpener(error=urllib.error.URLError("unreachable"))

    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(opener).fetch_questions(10)


def test_fetch_questions_raises_on_timeout() -> None:
    opener = FakeOpener(error=TimeoutError("slow"))

    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(opener).fetch_questions(10)


def test_fetch_questions_raises_on_http_429() -> None:
    error = urllib.error.HTTPError(
        "https://example.invalid",
        429,
        "Too Many Requests",
        Message(),
        io.BytesIO(),
    )

    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(FakeOpener(error=error)).fetch_questions(10)


def test_fetch_questions_raises_on_invalid_json() -> None:
    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(FakeOpener(b"<html>")).fetch_questions(10)


def test_fetch_questions_raises_on_missing_keys() -> None:
    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(FakeOpener(b'{"foo": 1}')).fetch_questions(10)


def test_fetch_questions_raises_on_non_zero_response_code() -> None:
    with pytest.raises(QuestionSourceError):
        OpenTriviaClient(FakeOpener(_body(response_code=1))).fetch_questions(10)
