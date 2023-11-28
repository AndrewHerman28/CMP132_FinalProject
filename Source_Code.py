import random
import tkinter as tk
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


class HigherOrLowerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Higher or Lower Game")
        self.geometry("400x400")

        self.money_label = tk.Label(self, text="Money: $0")
        self.money_label.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.value_label = tk.Label(self, text="Current Value: 5")
        self.value_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Game", command=self.play_game)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

        self.higher_button = tk.Button(self, text="Higher", command=lambda: self.make_guess("higher"))
        self.lower_button = tk.Button(self, text="Lower", command=lambda: self.make_guess("lower"))

        self.value = 5
        self.multiplier = 1
        self.temp_money = 0

        self.playing = False
        self.value_var = tk.StringVar()

    def play_game(self):
        self.playing = True
        self.start_button.pack_forget()
        self.higher_button.pack(pady=10)
        self.lower_button.pack(pady=10)

        # self.temp_money = 0
        self.multiplier = 1
        self.value = 5

        self.update_money_label()
        self.result_label.config(text="")
        self.value_label.config(text=f"Current Value: {self.value}")
        self.higher_button.config(state=tk.NORMAL)
        self.lower_button.config(state=tk.NORMAL)

        self.update_gui()

    def update_gui(self):
        if self.playing:
            self.after(100, self.update_gui)
            self.update_money_label()

    def make_guess(self, guess):
        self.higher_button.config(state=tk.DISABLED)
        self.lower_button.config(state=tk.DISABLED)

        new_value = random.randint(1, 10)

        self.result_label.config(text=f"The new value was: {new_value}")

        if (guess == "higher" and new_value > self.value) or (guess == "lower" and new_value < self.value):
            self.temp_money += self.multiplier
            self.multiplier += 1
            self.result_label.config(text="Correct! Great Job!")
        else:
            self.end_game()

        self.value = new_value
        self.value_label.config(text=f"Current Value: {self.value}")

        self.higher_button.config(state=tk.NORMAL)
        self.lower_button.config(state=tk.NORMAL)

    def update_money_label(self):
        self.money_label.config(text=f"Money: ${self.temp_money}")

    def end_game(self):
        self.result_label.config(text="Good Try! But that is incorrect")
        self.higher_button.config(state=tk.DISABLED)
        self.lower_button.config(state=tk.DISABLED)
        self.playing = False
        self.start_button.pack(pady=10)

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
            higher_lower_gui = HigherOrLowerGUI()
            higher_lower_gui.mainloop()
            money += higher_lower_gui.temp_money
            print("Money Earned:", higher_lower_gui.temp_money)
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
