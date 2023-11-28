# Computer Science 132 Final Project
The goal for this repository contains a collection of three different games related to gambling. While that may sound pretty bad at first there will be no real life money at stake during this process. The reward for completing the games is a long list of compliments for you to fell better about yourself. The amount of compliments gained is proportional to the score you attain when completing the series of games.
## Games Included
1. Blackjack:
  * A classic card game where the goal is to have a hand value as close to 21 as possible without exceeding it. The numbers are constrained to a standard deck of cards.
2. Higher or Lower:
  * Guess whether the next random number will be higher or lower than the current number. The numbers are constrained to a standard deck of cards.
3. Plinko!:
  * A game of plinko where a ball is dropped and is randomly placed into nine different columns which holds different values.

## How to Play:
* Blackjack:
Run the given code and select Blackjack by entering in b or B into the console.
Follow the prompts to hit or stand and try to get a hand value as close to 21 as possible without exceeding it.
Receive feedback and compliments based on the game outcome.

* Higher or Lower:
Run the given code and select Higher or Lower by entering in h or H into the console.
Guess whether the next random number will be higher or lower than the current number.
Accumulate money for each correct guess and receive compliments.

* Plinko:
Run the given code and select Plinko by entering in p or P into the console.
Click the "Start Plinko" button to drop the ball.
The ball will bounce off pegs(that are not shown), and the final position determines the score.
Receive compliments based on your score.

## Code Structure
This section is to show how each class contributed to the overall code.

* Plinko Game:

The Plinko game is implemented using the tkinter library for the graphical user interface. 
The main class PlinkoGUI handles the game window and user interaction.
The Ball class represents the ball in the Plinko game, managing its movement and position.
The game logic is divided into methods such as draw_plinko_board, play_game, get_result, drop_ball, and display_results.

* Blackjack:

The Blackjack game is implemented as a class BlackJack containing methods for playing the game.
Card values, player hands, and game outcomes are managed within the Backjack class.
User prompts and game feedback are displayed in the console.

* Higher or Lower:

The Higher or Lower game is implemented using Tkinter for the graphical user interface.
The main class HigherOrLowerGUI handles the game window, user interaction, and GUI elements.
The game logic is divided into methods such as play_game, make_guess, end_game, and update_money_label.
Random numbers and user guesses determine the game outcomes.

* Main Game Loop:

The main game loop allows users to choose between different games or view their current balance.
The loop continues until the user decides to quit ("Q").
The user's balance is tracked globally and updated based on the outcomes of each game.

* Compliments:

A series of positive compliments is stored in a list
Compliments are randomly selected and displayed to the user as a reward after playing a game.
The amount of compliments is equal to the amount of money obtained after quiting the game.

## Testing the Code.
### Opening Each Game
test- 
* game_type = input()
results-
* Blackjack: Successfully opens Blackjack
* Higher or Lower: Successfully opens Higher or Lower
* Plinko: Successfully opens Plinko


## How Justin learned GUI in python
https://www.youtube.com/watch?v=ibf5cx221hk&ab_channel=NeuralNine
