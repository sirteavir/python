height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))

bmi = weight/(height ** 2)
if bmi < 18.5:
    print("you are underweight")
elif 18.5 <=bmi < 25.0:
    print("you have a normal weight")
elif 25 <= bmi < 30.0:
    print("you are overweight")
else:
    print("you are obese")
