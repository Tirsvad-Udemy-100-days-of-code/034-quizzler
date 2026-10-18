🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

# Usage

## Run

With the `.venv` active:

```bash
python -m quizzler
```

An internet connection is needed to fetch ten true/false questions.

## How to play

Read the question and press the green check (True) or the red cross (False). The question box turns green for a right answer and red for a wrong one, the score in the top right goes up, and the next question follows after one second. After the last question the buttons are disabled and the final score is shown.

![Question](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/question.png)
![Right answer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/right-answer.png)
![Wrong answer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/wrong-answer.png)

## When something goes wrong

If the question service cannot be reached, a window with a short message is shown and the program ends with exit code 1. Check your internet connection and try again.
