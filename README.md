# QuizBrain  
## Description  
Welcome to QuizBrain! This is a simple command-line and graphical user interface (GUI) quiz game written in Python. The game fetches quiz questions from the Open Trivia Database and presents them to the user. Players can answer true/false questions, and the game provides feedback on correctness and calculates the final score.  
## Features  
- Command-line and GUI interfaces
- Open Trivia Database integration
- Score tracking
- Visual feedback for correct and incorrect answers  
## Screenshots  
![Quiz Game GUI](screenshots/quiz_game_gui.png)  
## Installation  
1. Clone the repository:     `https://github.com/yassergribi/QuizBrain.git`

2.  Navigate to the project directory:
        
    `cd quizbrain`
    
3.  Install dependencies:
        
    `pip install -r requirements.txt`
    
4.  Run the game:
        
    `python main.py`
    

Usage
-----

*   Run the game using the command above.
*   Answer the true/false questions in the GUI.
*   The game will provide feedback on each answer, and your final score will be displayed at the end.

Dependencies
------------

*   Python 3.x
*   `requests` library for fetching quiz questions
*   `tkinter` library for the GUI

Project Structure
-----------------

*   `main.py`: Entry point for running the game.
*   `quiz_brain.py`: Contains the QuizBrain class for managing the quiz logic.
*   `images/`: Directory containing images used in the GUI.
*   `screenshots/`: Directory containing screenshots for the README.

Contributing
------------

If you'd like to contribute to the development of this Quiz Game, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3.  Make your changes and commit them: `git commit -m 'Your message here'`.
4.  Push your changes to your fork: `git push origin feature-name`.
5.  Submit a pull request.

License
-------

This Quiz Game is open-source and available under the MIT License.