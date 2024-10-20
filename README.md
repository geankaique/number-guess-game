# Number Guessing game
Welcome to the Number Guessing Game! This is a CLI-based game where the user has to guess a number between 1 and 100. The user has a limited number of chances based on the difficulty level.

This is an educational purpose project created for [roadmap.sh](https://roadmap.sh/projects/number-guessing-game)

# Sample 
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Select the difficulty level: 
[ 1 ] Easy (10 chances)
[ 2 ] Medium (5 chances)
[ 3 ] Hard (3 chances)
Enter your choice: 2
You have selected the Medium difficulty level.
Let's start the game!

Choose a Number between 1 and 100: 50
Incorrect! The number is greater than 50.
Choose a Number between 1 and 100: 90
Incorrect! The number is less than 90.
Choose a Number between 1 and 100: 88
Congratulations you beat the game with 3 attempts

Play again? [Y/N] 
``` 

# Features

* Select a difficulty level to determine the number of chances: 
  * Easy: 10 chances
  * Medium: 5 chances
  * Hard: 3 chances
* Receive feedback on whether your guess is too high or too low.
* Track the number of attempts.
* Play multiple rounds

# Installation
Clone the repository:

`git clone https://github.com/geankaique/number-guess-game.git`

`cd number-guessing-game`

# How to Play
Inside the program directory

`cd number-guess` 

`python app.py`

# Requirements
Python
