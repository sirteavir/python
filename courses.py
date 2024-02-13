class Course:
    def __init__(self,Course, Rate):
        self.Course = Course
        self.Rate = Rate
    def display(self):
        print(f"One of the courses is {self.Course} "
              f"and the chances of me doing it is {self.Rate}")
myobj= Course("Medicine","0/10")
myobj2 = Course("Law","1/10")
myobj3 = Course("CompScie","8/10")
myobj4 = Course("Teaching","2/10")
myobj5 = Course("Fashion", "5/10")

myobj.display()
myobj2.display()
myobj3.display()
myobj4.display()
myobj5.display()