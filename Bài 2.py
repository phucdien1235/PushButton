from guizero import App, PushButton, Box, Text
from random import randint
def random():
    random_number = randint(1, 100)
    random_text.value = str(random_number)
app = App(title = "Random", width = 200, height = 150)
box_hide_top = Box(app, width = "fill", height = 65)
random_button = PushButton(app, width = 14, height = 1, text = "Click here to random", command = random)
box_hide_bottom = Box(app, width = "fill", height = 65)
random_text = Text(box_hide_bottom, text = None, color = "red")

app.display()