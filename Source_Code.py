import random
import tkinter as tk
from tkinter import messagebox
money = 0

happiness_phrases = [
    "You're Awesome!",
    "You make a difference.",
    "You're doing great!",
    "You're a ray of sunshine.",
    "You're a star!",
    "Your smile is contagious.",
    "You're making progress.",
    "You're loved and appreciated.",
    "You bring joy to others.",
    "You're fantastic!",
    "You're making a positive impact.",
    "You've got this!",
    "You're a source of inspiration.",
    "You're full of positivity.",
    "You're a wonderful person.",
    "You're a beacon of happiness.",
    "You're special and unique.",
    "You're spreading kindness.",
    "You light up the room.",
    "Your presence is a gift.",
    "You're making the world brighter.",
    "You're worth it!",
    "You're cherished by those around you.",
    "You're a true gem.",
    "You're a joy to be around.",
    "You're extraordinary!",
    "You make the world a better place.",
    "You're a blessing in disguise.",
    "You bring happiness wherever you go."
]


class Ball:
    def __init__(self, canvas, slot, slot_width):
        self.canvas = canvas
        self.slot = slot
        self.slot_width = slot_width
        self.radius = 10
        self.y = 10  # Initial y-coordinate
        self.ball = self.canvas.create_oval(self.get_ball_coords(), fill="blue")

    def get_ball_coords(self):
        x = (self.slot + 0.5) * self.slot_width
        return x - self.radius, self.y - self.radius, x + self.radius, self.y + self.radius

    def move(self):
        direction = random.choice([-1, 1])
        self.slot += direction
        self.slot = max(0, min(num_slots - 1, self.slot))
        self.y += 20  # Move the ball down
        self.canvas.coords(self.ball, self.get_ball_coords())
        return self.y

    def get_final_slot(self):
        return self.slot


class PlinkoGUI(tk.Tk):
    def __init__(self, num_slots):
        super().__init__()

        self.title("Plinko Game")
        self.geometry("800x600")

        self.num_slots = num_slots
        self.slot_width = 800 / self.num_slots
        self.slots = [0] * self.num_slots

        self.canvas = tk.Canvas(self, width=800, height=400, bg="white")
        self.canvas.pack(pady=20)

        self.close_button = tk.Button(self, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

        self.results_label = tk.Label(self, text="")
        self.results_label.pack(pady=10)

    def draw_plinko_board(self):
        for i in range(self.num_slots + 1):
            x = i * self.slot_width
            self.canvas.create_line(x, 0, x, 400, fill="black")

    def play_game(self):
        self.clear_canvas()
        self.slots = [0] * self.num_slots
        num_balls = 1

        for _ in range(num_balls):
            ball = Ball(self.canvas, random.randint(0, self.num_slots - 1), self.slot_width)
            final_slot = self.drop_ball(ball)

        self.display_results()
        return self.get_result(final_slot)

    def get_result(self, final_slot):
        if final_slot == 0:
            return 1
        elif final_slot == 1:
            return 3
        elif final_slot == 2:
            return 5
        elif final_slot == 3:
            return 7
        elif final_slot == 4:
            return 10
        elif final_slot == 5:
            return 7
        elif final_slot == 6:
            return 5
        elif final_slot == 7:
            return 3
        elif final_slot == 8:
            return 1

    def drop_ball(self, ball):
        while ball.move() < 400:
            self.update()
            self.after(50)  # Delay for visualization

        final_slot = ball.get_final_slot()
        self.slots[final_slot] += 1
        return final_slot

    def display_results(self):
        results_text = "Results:\n"
        for i, count in enumerate(self.slots):
            results_text += f"Slot {i}: {count} balls\n"

        self.results_label.config(text=results_text)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_plinko_board()

    def close_window(self):
        self.destroy()


class BlackJack:
    def __init__(self):
        self.money = 0

    def play_blackjack(self):
        player_cards = []
        dealer_cards = []
        player_score = 0
        dealer_score = 0

        for _ in range(2):
            player_cards.append(random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']))
            dealer_cards.append(random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']))

        for card in player_cards:
            print("Card Value ", card)
            if card == 'A':
                player_score += 11
            elif card in ['J', 'Q', 'K']:
                player_score += 10
            else:
                player_score += int(card)

        print("Your Sum:", player_score)

        if player_score == 21:
            print("Blackjack! You win!")
            return 5

        while True:
            hit = input("Hit or stand? ")
            if hit.lower() == 'hit' or hit.lower() == "h":
                player_card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
                print("New Card ", player_card)
                player_cards.append(player_card)

                if player_card == 'A':
                    player_score += 11
                elif player_card in ['J', 'Q', 'K']:
                    player_score += 10
                else:
                    player_score += int(player_card)

                print("Total Sum", player_score)

                if player_score > 21:
                    print("You busted! You lose.")
                    return 1
            else:
                break

        while dealer_score < 17:
            dealer_card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
            dealer_cards.append(dealer_card)

            if dealer_card == 'A':
                dealer_score += 11
            elif dealer_card in ['J', 'Q', 'K']:
                dealer_score += 10
            else:
                dealer_score += int(dealer_card)

        print("Dealer Sum: ", dealer_score)

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


class HigherOrLowerGame:
    def __init__(self):
        self.money = 0

    def start(self):
        temp_money = 0
        multiplier = 1
        value = 5

        while True:
            action = input(f"Higher or Lower than:  {value}\nType (H) Higher or (L) Lower or (Q) quit\nType Here: ")
            new_value = random.randint(1, 10)

            if action.lower() == "q":
                break

            print("The new value was: ", new_value)

            if action.lower() == "h":
                if new_value > value:
                    print("Correct! Great Job!")
                    temp_money += multiplier
                else:
                    print("Good Try! But that is incorrect")
                    break

            if action.lower() == "l":
                if new_value < value:
                    print("Correct! Great Job!")
                    temp_money += multiplier
                else:
                    print("Good Try! But that is incorrect")
                    break

            value = new_value
            multiplier += 1
            print("Money Earned: ", temp_money)


        self.money += temp_money
        return self.money

if __name__ == "__main__":
    running = True

    while running:
        game_type = input("Type (B) Blackjack\nType (H) Higher or Lower\nType (P) Plinko\nType (M) View Balance\nType (Q) to quit\nType Here: ")

        if game_type.lower() == "q":
            running = False
        elif game_type.lower() == "m":
            print("Balance: ", money)
        elif game_type.lower() == "b":
            blackjack_game = BlackJack()
            money += blackjack_game.play_blackjack()
        elif game_type.lower() == "h":
            higher_lower_game = HigherOrLowerGame()
            money += higher_lower_game.start()
        elif game_type.lower() == "p":
            num_slots = 9
            plinko_gui = PlinkoGUI(num_slots)
            plinko_gui.draw_plinko_board()
            final_result = plinko_gui.play_game()
            money += final_result
            print("Money Earned:", final_result)
           


print("You have earned $", money, "! Here are", money, "compliments!")
for i in range(money):
    print(random.choice(happiness_phrases))
