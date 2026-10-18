"""Errors raised by the business rules of the quiz."""


class QuizFinishedError(Exception):
    """@brief Raised when a question is requested but none is left."""


class NoCurrentQuestionError(Exception):
    """@brief Raised when an answer is checked before a question was asked."""
