"""Constants of the Quizzler application.

Documentation style: Doxygen ``##`` comment blocks with ``@brief`` placed
directly above each constant, and ``@name`` groups.
"""

from typing import Final

## @name Open Trivia Database
## @{

## @brief Endpoint of the Open Trivia Database question API.
API_URL: Final[str] = "https://opentdb.com/api.php"

## @brief Number of questions requested per game.
QUESTION_AMOUNT: Final[int] = 10

## @brief Question type requested from the API (true/false questions).
QUESTION_TYPE: Final[str] = "boolean"

## @brief Seconds to wait for the API before giving up.
REQUEST_TIMEOUT_SECONDS: Final[int] = 10

## @}

## @name Answers
## @{

## @brief Text of the "true" answer, as the API returns it.
TRUE_ANSWER: Final[str] = "True"

## @brief Text of the "false" answer, as the API returns it.
FALSE_ANSWER: Final[str] = "False"

## @}

## @name User interface
## @{

## @brief Background color of the window (from the course ui.py).
THEME_COLOR: Final[str] = "#375362"

## @brief Title of the main window.
WINDOW_TITLE: Final[str] = "Quizzler"

## @brief Padding around the window content, in pixels.
WINDOW_PADDING: Final[int] = 20

## @brief Width of the question canvas, in pixels.
CANVAS_WIDTH: Final[int] = 300

## @brief Height of the question canvas, in pixels.
CANVAS_HEIGHT: Final[int] = 250

## @brief Normal background color of the question canvas.
CANVAS_BACKGROUND: Final[str] = "white"

## @brief Canvas color flashed after a right answer.
CANVAS_RIGHT_COLOR: Final[str] = "green"

## @brief Canvas color flashed after a wrong answer.
CANVAS_WRONG_COLOR: Final[str] = "red"

## @brief Width at which the question text wraps, in pixels.
QUESTION_WRAP_WIDTH: Final[int] = 280

## @brief Font of the question text: family, size, style.
QUESTION_FONT: Final[tuple[str, int, str]] = ("Arial", 20, "italic")

## @brief Font of the score label: family, size.
SCORE_FONT: Final[tuple[str, int]] = ("Arial", 12)

## @brief Text color of the score label.
SCORE_TEXT_COLOR: Final[str] = "white"

## @brief Milliseconds the right/wrong feedback color stays visible.
FEEDBACK_DELAY_MS: Final[int] = 1000

## @brief Name of the folder that holds the button images.
IMAGE_DIRECTORY_NAME: Final[str] = "images"

## @brief File name of the "true" button image.
TRUE_IMAGE_NAME: Final[str] = "true.png"

## @brief File name of the "false" button image.
FALSE_IMAGE_NAME: Final[str] = "false.png"

## @brief Vertical padding around the question canvas, in pixels.
CANVAS_PADDING_Y: Final[int] = 50

## @brief Question text color while the canvas shows right/wrong feedback.
FEEDBACK_TEXT_COLOR: Final[str] = "white"

## @brief Position of the question text inside the canvas (x, y).
CANVAS_QUESTION_POSITION: Final[tuple[int, int]] = (150, 125)

## @brief Padding around the true/false buttons, in pixels.
BUTTON_PADDING: Final[int] = 0

## @brief Prefix of the score label text.
SCORE_LABEL_PREFIX: Final[str] = "Score: "

## @brief Text shown when all questions have been answered.
FINISHED_TEXT: Final[str] = "You have reached the end of the quiz."

## @brief Text shown when the questions could not be loaded.
ERROR_TEXT: Final[str] = "Quizzler could not load the questions."

## @brief Width at which the error message wraps, in pixels.
ERROR_WRAP_WIDTH: Final[int] = 300

## @}
