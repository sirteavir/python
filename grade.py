marks=int(input("Enter Marks Scored:"))

if marks>=80 and marks<=100:
    print("You have scored A")
elif marks>=60 and marks<=79:
    print("You have scored B")
elif marks>=40 and marks<=59:
    print("you have scored C")
elif marks>=0 and marks<=39:
    print("You have scored an E")
else:
    print("Invalid marks")