from guizero import  App, Text, PushButton, Box, info
app = App(title = "Quiz app", width = 300, height = 200)
question = Text(app, text = "Thủ đô của Việt Nam là tỉnh nào?", size = 15, color = "red")
box_answer = Box(app, width = 300, height = 180)
def real_answer(answer):
    if answer == "Hà Nội":
        info("Thông báo", "You win!!!")
    else:
        info("Thông báo", "You lose")
answer_1 = PushButton(box_answer, text = "TP.HCM", align = "left", width = 10, height = 6, command = real_answer, args = ["TP.HCM"])
answer_2 = PushButton(box_answer, text = "Hà Nội", align = "left", width = 10, height = 6, command = real_answer, args = ["Hà Nội"])
answer_3 = PushButton(box_answer, text = "Đà Nẵng", align = "left", width = 10, height = 6, command = real_answer, args = ["Đà Nẵng"])

app.display()