from guizero import App, Box, PushButton, Picture
on_or_off_1 = 0
on_or_off_2 = 0
on_or_off_3 = 0
app = App(title = "LED control", width = 396, height = 300)
def turn_on_or_turn_off(button):
    global on_or_off_1, on_or_off_2, on_or_off_3
    if button == 1:
        if on_or_off_1 == 0:
            pic_LED_1.image = "Bật.png"
            on_or_off_1 += 1
        elif on_or_off_1 == 1:
            pic_LED_1.image = "Tắt.png"
            on_or_off_1 -= 1
    if button == 2:
        if on_or_off_2 == 0:
            pic_LED_2.image = "Bật.png"
            on_or_off_2 += 1
        elif on_or_off_2 == 1:
            pic_LED_2.image = "Tắt.png"
            on_or_off_2 -= 1
    if button == 3:
        if on_or_off_3 == 0:
            pic_LED_3.image = "Bật.png"
            on_or_off_3 += 1
        elif on_or_off_3 == 1:
            pic_LED_3.image = "Tắt.png"
            on_or_off_3 -= 1
box_LED = Box(app, width = 396, height = 270)
box_LED_1 = Box(box_LED, width = 132, height = 270, align = "left", border = True)
box_LED_2 = Box(box_LED, width = 132, height = 270, align = "left", border = True)
box_LED_3 = Box(box_LED, width = 132, height = 270, align = "left", border = True)
pic_LED_1 = Picture(box_LED_1, image = None)
pic_LED_2 = Picture(box_LED_2, image = None)
pic_LED_3 = Picture(box_LED_3, image = None)
box_button = Box(app, width = 396, height = 30)
PushButton(box_button, text = "Nút 1", align = "left", width = 15, height = 3, command = turn_on_or_turn_off, args = [1])
PushButton(box_button, text = "Nút 2", align = "left", width = 15, height = 3, command = turn_on_or_turn_off, args = [2])
PushButton(box_button, text = "Nút 3", align = "left", width = 15, height = 3, command = turn_on_or_turn_off, args = [3])

app.display()