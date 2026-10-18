"""View of the quiz screen: the course's class-based tkinter GUI."""

import tkinter
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from quizzler.constants import (
    BUTTON_PADDING,
    CANVAS_BACKGROUND,
    CANVAS_HEIGHT,
    CANVAS_PADDING_Y,
    CANVAS_QUESTION_POSITION,
    CANVAS_RIGHT_COLOR,
    CANVAS_WIDTH,
    CANVAS_WRONG_COLOR,
    ERROR_WRAP_WIDTH,
    FALSE_IMAGE_NAME,
    FEEDBACK_DELAY_MS,
    FEEDBACK_TEXT_COLOR,
    IMAGE_DIRECTORY_NAME,
    QUESTION_FONT,
    QUESTION_WRAP_WIDTH,
    SCORE_FONT,
    SCORE_TEXT_COLOR,
    THEME_COLOR,
    TRUE_IMAGE_NAME,
    WINDOW_PADDING,
    WINDOW_TITLE,
)
from quizzler.domain.quiz_brain import QuizBrain
from quizzler.presentation.quiz_view_model import QuizViewModel

_IMAGE_DIRECTORY = Path(__file__).parent / IMAGE_DIRECTORY_NAME


def _make_window() -> tkinter.Tk:
    """@brief Create a themed top-level window.

    @return The window with title, padding and background set.
    """
    window = tkinter.Tk()
    window.title(WINDOW_TITLE)
    window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=THEME_COLOR)
    return window


class QuizInterface:
    """@brief The quiz window: score, question canvas and two answer buttons."""

    def __init__(self, quiz_brain: QuizBrain) -> None:
        """@brief Build the window and show the first question.

        The main loop is not entered; call run().

        @param quiz_brain The quiz to play.
        """
        self.view_model: QuizViewModel = QuizViewModel(quiz_brain)
        self.window: tkinter.Tk = _make_window()
        self.score_label: tkinter.Label = self._build_score_label()
        self.canvas: tkinter.Canvas = self._build_canvas()
        self.question_text: int = self._build_question_text()
        # Kept on self: tkinter does not hold a reference to its images.
        self.true_image: tkinter.PhotoImage = self._load_image(TRUE_IMAGE_NAME)
        self.false_image: tkinter.PhotoImage = self._load_image(FALSE_IMAGE_NAME)
        self.true_button: tkinter.Button = self._build_button(
            self.true_image, self.true_pressed, column=0
        )
        self.false_button: tkinter.Button = self._build_button(
            self.false_image, self.false_pressed, column=1
        )
        self.get_next_question()

    def run(self) -> None:
        """@brief Enter the tkinter main loop until the window is closed."""
        self.window.mainloop()

    def get_next_question(self) -> None:
        """@brief Reset the canvas and show the next text.

        Disables both buttons when the quiz is finished.
        """
        self.canvas.config(bg=CANVAS_BACKGROUND)
        text = self.view_model.get_next_question()
        self.canvas.itemconfig(self.question_text, text=text, fill=THEME_COLOR)
        self._set_buttons_state(
            tkinter.DISABLED if self.view_model.is_finished else tkinter.NORMAL
        )

    def true_pressed(self) -> None:
        """@brief Handle a click on the true button."""
        self.give_feedback(self.view_model.answer_true())

    def false_pressed(self) -> None:
        """@brief Handle a click on the false button."""
        self.give_feedback(self.view_model.answer_false())

    def give_feedback(self, is_correct: bool) -> None:
        """@brief Flash the canvas, update the score and queue the next question.

        @param is_correct Whether the answer was right.
        """
        color = CANVAS_RIGHT_COLOR if is_correct else CANVAS_WRONG_COLOR
        self.canvas.config(bg=color)
        self.canvas.itemconfig(self.question_text, fill=FEEDBACK_TEXT_COLOR)
        self._set_buttons_state(tkinter.DISABLED)
        self.score_label.config(text=self.view_model.score_text)
        self.window.after(FEEDBACK_DELAY_MS, self.get_next_question)

    def _set_buttons_state(self, state: Literal["normal", "disabled"]) -> None:
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def _build_score_label(self) -> tkinter.Label:
        label = tkinter.Label(
            self.window,
            text=self.view_model.score_text,
            fg=SCORE_TEXT_COLOR,
            bg=THEME_COLOR,
            font=SCORE_FONT,
        )
        label.grid(row=0, column=1)
        return label

    def _build_canvas(self) -> tkinter.Canvas:
        canvas = tkinter.Canvas(
            self.window,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=CANVAS_BACKGROUND,
            highlightthickness=0,
        )
        canvas.grid(row=1, column=0, columnspan=2, pady=CANVAS_PADDING_Y)
        return canvas

    def _build_question_text(self) -> int:
        x, y = CANVAS_QUESTION_POSITION
        return self.canvas.create_text(
            x,
            y,
            width=QUESTION_WRAP_WIDTH,
            font=QUESTION_FONT,
            fill=THEME_COLOR,
        )

    def _load_image(self, file_name: str) -> tkinter.PhotoImage:
        return tkinter.PhotoImage(
            master=self.window, file=str(_IMAGE_DIRECTORY / file_name)
        )

    def _build_button(
        self,
        image: tkinter.PhotoImage,
        command: Callable[[], None],
        column: int,
    ) -> tkinter.Button:
        button = tkinter.Button(
            self.window,
            image=image,
            highlightthickness=0,
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING,
            command=command,
        )
        button.grid(row=2, column=column)
        return button


def show_error(message: str) -> None:
    """@brief Show a themed window with an error message and wait until closed.

    @param message The text to show.
    """
    window = _make_window()
    tkinter.Label(
        window,
        text=message,
        wraplength=ERROR_WRAP_WIDTH,
        fg=SCORE_TEXT_COLOR,
        bg=THEME_COLOR,
        font=SCORE_FONT,
    ).grid(row=0, column=0)
    window.mainloop()
