print("Welcome to BMI Calculator!")
weight = float(input("Enter your weight in kilogram(kg)\n> "))
height = float(input("Enter your height in meters(m2)\n> "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18:
    print("You're underweight", bmi)

elif bmi < 24.9:
    print("You're normal", bmi)

elif bmi < 29.9:
    print("You're overweight", bmi)

else:
    print("You're obese", bmi)
