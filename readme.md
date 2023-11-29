# Computer Science 132 Final Project
The goal for this repository is a collection of three different games related to gambling. While that may sound pretty bad at first there will be no real life money at stake during this process. The reward for completing the games is a long list of compliments for you to fell better about yourself. The amount of compliments gained is proportional to the score you attain when completing the series of games.
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





## Testing the Code

### Opening Each Game
#### Test Input
```python 3
game_type = input("Type (B) Blackjack\nType (H) Higher or Lower\nType (P) Plinko\nType (M) View Balance\nType (Q) to quit\nType Here: ")

game_function = game_functions.get(game_type.lower())
if game_function:
   game_function()
```
* Blackjack: Successfully opens Blackjack
* Higher or Lower: Successfully opens Higher or Lower
* Plinko: Successfully opens Plinko

### Testing Blackjack

#### Hit
```python 3
while True:
  hit = input("Hit (H) or Stand (S)?\nType Here: ")
  if hit.lower() == 'hit' or hit.lower() == "h":
     player_card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
     print("New Card ", player_card)
     player_cards.append(player_card)
```
Successfully adds a new card to user pile

#### Stand
```python 3
else:
  break
```
Successfully ends the users round


#### Win/Lose Condition
```python 3
if player_score == 21:
   print("You got blackjack! Amazin Job!")
   return 5
if player_score > 21:
   print("You busted! You lose.")
   return 1
if dealer_score == 21:
   print("Dealer blackjack! Good Try!")
   return 1
elif dealer_score > 21:
   print("Dealer Busted! You Win. Amazing Job!")
   return 5
if player_score > dealer_score:
   print("You win! You're Awesome!")
   return 5
elif player_score < dealer_score:
   print("Dealer Wins. You got it next time!")
   return 1
else:
   print("Push.")
   return 1
```
Successfully determines who wins and the appropriate amount of money is given to user



### Testing Higher or Lower

#### Start Game
```python 3
self.start_button = tk.Button(self, text="Start New Game", command=self.play_game)
self.start_button.pack(pady=10)

def play_game(self):
        self.playing = True
        self.start_button.pack_forget()
        self.higher_button.pack(pady=10)
        self.lower_button.pack(pady=10)

        self.multiplier = 1
        self.value = 5

        #Updates the value of the players money that shows at the top of the screen
        self.update_money_label()
        self.result_label.config(text="")
        self.value_label.config(text=f"Current Value: {self.value}")
        self.higher_button.config(state=tk.NORMAL)
        self.lower_button.config(state=tk.NORMAL)
```
Successfully starts game

#### Guess Higher/Lower
```python 3
#if the guess is higher and that is correct or if the guess is lower and correct then reward player
        if (guess == "higher" and new_value > self.value) or (guess == "lower" and new_value < self.value):
            self.temp_money += self.multiplier
            #The multiplier rewards more points each round for their streak that they are on
            self.multiplier += 1
            self.result_label.config(text="Correct! Great Job!")
        else:
            self.end_game()
```
Successfully checks higher or lower



#### Quit --> Successfully Closes window and adds money to user
#### Win/Lose Conditions
* Successfully continues round when guess is valid
* Successfully ends current round when guess is incorrect

### Testing Plinko


#### Dropping Plinko Ball
```python 3
def drop_ball(self, ball):
        while ball.move() < 400:
            self.update()
            self.after(50)  # Delay for visualization

        final_slot = ball.get_final_slot()
        self.slots[final_slot] += 1
        return final_slot
```
Successfully drops plinko ball


#### Win Condition
```python 3
def get_result(self, final_slot):
        result_values = [1, 3, 5, 7, 10, 7, 5, 3, 1]
        return result_values[final_slot]
```
Successfully adds money corrisponding to value of column the plinko lands in



### Testing Quit Application
#### Quit --> Successfully Quits Application and runs compliment list



#### Compliment List
```python 3
#For each dollar made, they earn a compliment
print("You have earned $", money, "! Here are", money, "compliments!")
for i in range(money):
    print(random.choice(happiness_phrases))

```
 Successfully lists the amount of compliments for each dollar earned

## Conclusion
In conclusion, this repository presents a collection of three engaging games related to gambling: Blackjack, Higher or Lower, and Plinko. Despite the gambling theme, there is no real-life money at stake, and the reward for completing the games is a series of uplifting compliments designed to make players feel better about themselves. Overall, the project was a success. 
## Contributers
* Justin Kwak
* Andrew Herman
## How We learned GUI in python
https://www.youtube.com/watch?v=ibf5cx221hk&ab_channel=NeuralNine
