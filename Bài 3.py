from guizero import App, PushButton, Picture, Box
def changing_picture(picture):
    if picture == "Cat":
        pic.image = "Mèo.png"
    elif picture == "Dog":
        pic.image = "Chó.png"
    else:
        pic.image = "Chim.png"
app = App(title = "Image Viewer", width = 400, height = 350)
picture_box = Box(app, width = 250, height = 250, border = True)
pic = Picture(picture_box, image = None)
button_box = Box(app, width = 300, height = 100, border = True)
cat_button = PushButton(button_box, text = "Cat", align = "left", width = 11, height = 5, command = changing_picture, args = ["Cat"])
dog_button = PushButton(button_box, text = "Dog", align = "left", width = 11, height = 5, command = changing_picture, args = ["Dog"])
bird_button = PushButton(button_box, text = "Bird", align = "left", width = 11, height = 5, command = changing_picture, args = ["Bird"])

app.display()