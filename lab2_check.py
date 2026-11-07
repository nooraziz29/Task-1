from lab2_model import ClassroomAgent

classroom = ClassroomAgent()
inputs = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]
count = 1

for temp, occupied in inputs:
    mode, send_command = classroom.act(temp, occupied)

    print("Test number:", count)
    print("Temperature:", temp)
    print("Room occupied:", occupied)
    print("Selected mode:", mode)

    if send_command == True:
        print("Status: Command sent")
    else:
        print("Status: No new command")

    print()
    count += 1