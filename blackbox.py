weight= int(input("Enter your weight:"))
height = int(input("Enter your height:"))

def BMI(weight, height):
    # Calculate BMI using the provided formula
    bmi = weight / (height ** 2)

    # Determine BMI grade and return it
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
        else:
        return "Obesity"


# Prompt user for weight and height
weight = float(input("Input the weight (kg): "))
height = float(input("Input the height (m): "))

# Call the BMI function with provided weight and height
bmi_result = BMI(weight, height)
# Display the calculated BMI and the corresponding grade
print("BMI = {:.2f}".format(weight / (height ** 2)))
print(bmi_result)