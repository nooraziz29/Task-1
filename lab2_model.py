class ClassroomAgent:
    def __init__(self):
        self.last_mode = None

    def act(self, temp, occupied):
        if occupied == False:
            mode = "ECO"
        elif temp > 26:
            mode = "COOL"
        elif temp < 20:
            mode = "WARM"
        else:
            mode = "IDLE"

        if mode == self.last_mode:
            send = False
        else:
            send = True

        self.last_mode = mode
        return mode, send

agent = ClassroomAgent()

data = [(29, True), (29, True), (20, True),
        (26, True), (19, True), (29, False)]

for item in data:
    mode, send = agent.act(item[0], item[1])
    print(item, mode, send)