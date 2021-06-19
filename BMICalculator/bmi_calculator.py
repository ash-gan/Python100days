
def calulate_bmi():
    """
    user inputs
    weight(float): User Input
    height(float):  User Input
    :return:
    bmi(float):  weight/(height*height)
    """
    weight = float(input("What's your weight?: "))
    height = float(input("What's your height?: "))
    bmi = weight/(height**2)
    return bmi

bmi = calulate_bmi()
if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)} and you are underweight")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {round(bmi, 2)} and you are normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is {round(bmi, 2)} and you are over weight")
elif 30 < bmi < 35:
    print(f"Your BMI is {round(bmi, 2)} and you are  obese")
else:
    print(f"Your BMI is greater than 35 and you are clinically obese")