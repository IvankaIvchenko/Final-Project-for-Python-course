import tkinter as tk
import random

class HangmanGame:
    def __init__(self):
        self.word = self.pick_the_word().lower()
        self.guessed_word = '_' * len(self.word)
        self.attempts_left = 10
        self.letters_tried = []
        self.game_over = False

    def pick_the_word(self):
        with open('wordlist.txt') as f:
            return random.choice(f.readlines()).strip()

    def update_guessed_word(self, guessed_letter):
        guessed_word = ""
        letter_guessed = False
        for i in range(len(self.word)):
            if self.word[i] == guessed_letter.lower():
                letter_guessed = True
                guessed_word += guessed_letter
            else:
                guessed_word += self.guessed_word[i]
        self.guessed_word = guessed_word
        return letter_guessed

    def game_lost(self):
        self.game_over = True
        return f"Sorry, you ran out of attempts! The word was '{self.word}'. Better luck next time!"

    def game_won(self):
        self.game_over = True
        return "Congratulations, you have revealed the word! You WON!!!"

    def guess_letter(self, guessed_letter):
        if self.game_over:
            return None

        info_message = ""
        letter_guessed = self.update_guessed_word(guessed_letter)
        if letter_guessed:
            if "_" not in self.guessed_word:
                return self.game_won()
            info_message = "Great job! Keep going!"
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return self.game_lost()
            info_message = f"Ooops, you guessed wrong! Try again! You still have {self.attempts_left} attempts left!"

        self.letters_tried.append(guessed_letter)
        return info_message

class HangmanUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.label_info = tk.Label(root, text="Do you accept the Hangman challenge?", font=("Arial", 20))
        self.result_label = tk.Label(root, text="", font=("Arial", 18))
        self.label_prompt = tk.Label(root, text="", font=("Arial", 18))
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.button_new_game = tk.Button(root, text="Start New Game", command=self.start_new_game)

        self.setup_ui()
        self.hide_the_word()
        self.create_alphabet_buttons()

    def setup_ui(self):
        self.label_info.pack(pady=10)
        self.label_prompt.pack(pady=10)
        self.result_label.pack(pady=10)
        self.canvas.pack(pady=10)

    def hide_the_word(self):
        self.result_label.config(text=self.format_word(self.game.guessed_word).strip())

    def format_word(self, word):
        return " ".join(word)

    def draw_hangman(self):
        attempts_left = self.game.attempts_left
        if attempts_left == 9:
            self.canvas.create_line(50, 250, 150, 250, width=2)
        elif attempts_left == 8:
            self.canvas.create_line(100, 50, 100, 250, width=2)
        elif attempts_left == 7:
            self.canvas.create_line(100, 50, 200, 50, width=2)
        elif attempts_left == 6:
            self.canvas.create_line(200, 50, 200, 80, width=2)
        elif attempts_left == 5:
            self.canvas.create_oval(180, 80, 220, 120, width=2)
        elif attempts_left == 4:
            self.canvas.create_line(200, 120, 200, 180, width=2)
        elif attempts_left == 3:
            self.canvas.create_line(200, 140, 170, 160, width=2)
        elif attempts_left == 2:
            self.canvas.create_line(200, 140, 230, 160, width=2)
        elif attempts_left == 1:
            self.canvas.create_line(200, 180, 170, 210, width=2)
        elif attempts_left == 0:
            self.canvas.create_line(200, 180, 230, 210, width=2)

    def show_message(self, message, color):
        self.label_info.config(text=message)
        self.label_info.config(fg=color)

    def guess_letter(self, guessed_letter):
        info_message = self.game.guess_letter(guessed_letter)

        if info_message:
            if self.game.game_over:
                color = "green" if self.game.attempts_left > 0 else "red"
                self.show_message(info_message, color)
                self.show_new_game_button()
                self.remove_alphabet_buttons()
            else:
                color = "green" if "Great job!" in info_message else "red"
                self.show_message(info_message, color)

            self.result_label.config(text=self.format_word(self.game.guessed_word).strip())
            self.draw_hangman()
            self.update_alphabet_buttons()  # Update alphabet buttons state

    def show_new_game_button(self):
        self.canvas.pack_forget()  # Hide hangman canvas
        self.button_new_game.pack(pady=10)  # Show new game button

    def start_new_game(self):
        self.game.__init__()  # Reset the game
        self.button_new_game.pack_forget()  # Hide new game button
        self.canvas.pack(pady=10)  # Show canvas
        self.canvas.delete("all")  # Clear the canvas at the start of new game
        self.hide_the_word()  # Reset the guessed word display
        self.label_info.config(text="Do you accept the Hangman challenge?")  # Reset the label
        self.reset_alphabet_buttons()  # Reset the alphabet buttons
        self.create_alphabet_buttons()  # Recreate the alphabet buttons under the canvas

    def create_alphabet_buttons(self):
        self.alphabet_frame = tk.Frame(self.root)
        self.alphabet_buttons = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            button = tk.Button(self.alphabet_frame, text=letter, width=4,
                               command=lambda l=letter: self.on_alphabet_button_click(l))
            button.grid(row=0, column=alphabet.index(letter), padx=2, pady=2)
            self.alphabet_buttons.append(button)
        self.alphabet_frame.pack(pady=10)

        self.alphabet_frame.place(relx=0.5,y=500,anchor=tk.CENTER)

    def reset_alphabet_buttons(self):
        for button in self.alphabet_buttons:
            button.config(state="normal", relief="raised", bg="SystemButtonFace")

    def update_alphabet_buttons(self):
        for button in self.alphabet_buttons:
            letter = button.cget("text")
            if letter in self.game.letters_tried:
                button.config(state="disabled", relief="sunken", bg="gray")
            else:
                button.config(state="normal", relief="raised", bg="SystemButtonFace")

    def on_alphabet_button_click(self, letter):
        self.guess_letter(letter)
        self.update_alphabet_buttons()  # Update alphabet buttons state after each click

    def remove_alphabet_buttons(self):
        for button in self.alphabet_buttons:
            button.grid_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ivanka's Hangman Game")
    root.geometry("600x500")
    root.wm_minsize(1100, 600)

    game = HangmanGame()
    ui = HangmanUI(root, game)

    root.mainloop()