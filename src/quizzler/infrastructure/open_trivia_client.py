"""Client of the Open Trivia Database; implements the QuestionSource port."""

import json
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping, Sequence

from quizzler.application.errors import QuestionSourceError
from quizzler.constants import API_URL, QUESTION_TYPE, REQUEST_TIMEOUT_SECONDS

_SUCCESS_CODE = 0


def _open_url(url: str, timeout: float) -> bytes:
    """@brief Read the body of a URL over the network.

    @param url The address to read.
    @param timeout Seconds to wait before giving up.
    @return The response body.
    """
    with urllib.request.urlopen(url, timeout=timeout) as response:
        body: bytes = response.read()
    return body


class OpenTriviaClient:
    """@brief Fetches true/false questions from the Open Trivia Database."""

    def __init__(self, opener: Callable[[str, float], bytes] = _open_url) -> None:
        """@brief Create a client.

        @param opener Function that reads a URL with a timeout; replaceable in tests.
        """
        self._opener = opener

    def build_url(self, amount: int) -> str:
        """@brief Build the request URL.

        @param amount How many questions to request.
        @return The API URL with the amount and type parameters.
        """
        query = urllib.parse.urlencode({"amount": amount, "type": QUESTION_TYPE})
        return f"{API_URL}?{query}"

    def fetch_questions(self, amount: int) -> Sequence[Mapping[str, str]]:
        """@brief Fetch question records from the API.

        @param amount How many questions to request.
        @return The raw records of the "results" field.
        @throws QuestionSourceError On a network error, a bad response or an
            error response code.
        """
        url = self.build_url(amount)
        try:
            body = self._opener(url, REQUEST_TIMEOUT_SECONDS)
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            raise QuestionSourceError(
                f"Could not reach the question API: {err}"
            ) from err
        return self._parse(body)

    @staticmethod
    def _parse(body: bytes) -> Sequence[Mapping[str, str]]:
        """@brief Extract the records from a response body.

        @param body The raw JSON response.
        @return The records of the "results" field.
        @throws QuestionSourceError When the body is invalid or reports an error.
        """
        try:
            payload = json.loads(body)
            response_code = payload["response_code"]
            results: Sequence[Mapping[str, str]] = payload["results"]
        except (ValueError, KeyError, TypeError) as err:
            raise QuestionSourceError(f"Invalid response from the API: {err}") from err
        if response_code != _SUCCESS_CODE:
            raise QuestionSourceError(
                f"The API returned response code {response_code}."
            )
        return results
