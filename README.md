

# Trivia Quizzer

This repository contains a Python application that allows users to take a quiz with multiple choice or true/false questions.

## Requirements

- Python 3.6 or higher
- Tkinter (included with Python)


## How to Run

1. Clone or download the repository
2. Navigate to the directory containing the code
3. Run `python main.py`

## Code Structure

- `main.py`: The entry point for the application. It creates a `QuizBrain` object and a `QuizInterface` object and starts the main loop of the UI.
- `quiz_brain.py`: Contains the `QuizBrain` class, which manages the quiz logic such as selecting the next question and checking answers.
- `ui.py`: Contains the `QuizInterface` class, which handles the UI for the quiz application.
- `question.py`: Contains the `Question` class, which defines a quiz question with a question text and correct answer.
- `data.py`: Contains a list of dictionaries with quiz questions and answers.

## Screenshots

![Screenshot of the quiz UI](screenshots/screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






