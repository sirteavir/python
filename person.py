class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"My name is {self.name} "
              f"and my age is {self.age}")

myobj1 = person("Seanice",18)
myobj2 = person("John",2)
myobj3 = person("Latasha",18)
myobj4 = person("Reagan",4)
myobj5 = person("Neema",18)


myobj1.display()
myobj2.display()
myobj3.display()
myobj4.display()
myobj5.display()
