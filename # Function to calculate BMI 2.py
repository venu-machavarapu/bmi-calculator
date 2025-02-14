# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI formula
    return round(bmi, 2)

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Input weight and height from the user
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (cm): "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Output the result
print(f"Your BMI is: {bmi}")
print(f"BMI Category: {bmi_category(bmi)}")