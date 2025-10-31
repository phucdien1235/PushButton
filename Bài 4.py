from guizero import App, Text, Box, PushButton
from random import choice
def check(your_choice):
    computer_choice = choice(choices_lst)
    if your_choice == computer_choice:
        result.value = "Your choice:", your_choice, "|", "Computer choice:", computer_choice, "|", "Result: Tie"
    elif your_choice == "Rock" and computer_choice == "Scissors" or your_choice == "Paper" and computer_choice == "Rock" or your_choice == "Scissors" and computer_choice == "Paper":
        result.value = "Your choice:", your_choice, "|", "Computer choice:", computer_choice, "|", "Result: Win"
    else:
        result.value = "Your choice:", your_choice, "|", "Computer choice:", computer_choice, "|", "Result: Lose"
choices_lst = ["Rock", "Paper", "Scissors"]
app = App(title = "Rock Paper Scissors", width = 750, height = 300)
Text(app, text = "Chọn 1 trong 3:", size = 20, color = "red")
box_choices = Box(app, width = 300, height = 150, border = True)
rock_button = PushButton(box_choices, align = "left", width = 10, height = 5, text = "Rock", command = check, args = ["Rock"])
paper_button = PushButton(box_choices, align = "left", width = 10, height = 5, text = "Paper", command = check, args = ["Paper"])
scissors_button = PushButton(box_choices, align = "left", width = 10, height = 5, text = "Scissors", command = check, args = ["Scissors"])
result = Text(app, text = None, size = 15, color = "red")

app.display()