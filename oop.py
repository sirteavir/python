class series:
    def __init__(self, name, rate, airing):
        self.name = name
        self.rate = rate
        self.airing= airing
    def show(self):
        print(f"My favorite series is {self.name} "
              f"and i rate it at {self.rate} "
              f"and it is aired on {self.airing}")
myobj=series("OneDay","10/10", "Netflix")
myobj2=series("OuterBanks","8/10","Netflix")

myobj.show()
myobj2.show()




