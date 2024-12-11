README

Ivanka's Hangman Game

This project is a graphical implementation of the classic Hangman game built using Python and the Tkinter library. The game challenges players to guess a hidden word, one letter at a time, before running out of attempts.

Features

- Graphical Interface: A user-friendly interface with alphabet buttons for guessing letters and a canvas that displays the Hangman drawing.
- Dynamic Word Selection: Words are randomly chosen from a text file (wordlist.txt).
- Game States:
-- Displays progress as players guess letters.
-- Tracks incorrect guesses and reduces remaining attempts.
-- Ends the game with win/lose messages.
- Reset Option: Start a new game directly from the interface.
- Hangman Drawing: Visual feedback for incorrect guesses through progressive drawing of the Hangman figure.

Installation

1. Clone the Repository:
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
2. Ensure Python is Installed: This game requires Python 3.x. 
3. Install Required Libraries: Tkinter comes pre-installed with most Python distributions. No additional dependencies are needed.

How to Play

1. Run the Game:
python hangman.py
2. Start Guessing Letters:
- Use the buttons on the interface to guess letters.
- Correct guesses reveal letters in the hidden word.
- Incorrect guesses reduce attempts and draw parts of the Hangman.
3. Win or Lose:
- Win by guessing the entire word before running out of attempts.
- Lose when all parts of the Hangman are drawn.

File Structure

- hangman.py: Main script that contains the game logic and UI implementation.
- wordlist.txt: A list of possible words for the game.
-- Please ensure that the wordlist.txt file is located in the same folder as hangman.py!

Customization

Adding Words

To add more words to the game:
1. Open wordlist.txt.
2. Add new words, one per line.

License
This project is open-source and available under the MIT License. See the LICENSE file for details.

Enjoy playing the classic Hangman game! 🎉
