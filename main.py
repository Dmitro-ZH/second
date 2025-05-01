import random

class Student:

    def __init__(self, name):
        self.name = None
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("To study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False

    def nd_of_the_day(self):
        print(f"Gladness: {self.gladness}.\n"
              f"Progress: {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
