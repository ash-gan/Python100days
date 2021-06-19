
def tip_calculator():
    """
    Total bill(float): User Input
    Tip Percentage(int): User Input
    :return:
    person_bill(float):Round to 2 decimal places
    """
    total_bill = float(input("What is the total bill?: "))
    tip_percentage= int(input("What percentage of the tip you want?:"))
    num_of_people=int(input("How many people dividing the bill?:"))
    each_person_bill= (((tip_percentage*total_bill)/100)+total_bill)/num_of_people
    return round(each_person_bill,2)

bill = tip_calculator()
print(f"Each person should pay ${bill}.")
