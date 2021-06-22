import random

def get_random_person(list_of_people):
    ran_person = random.choice(list_of_people)
    return ran_person

list_of_people = input("Enter the members you went for dinner: ")
person_to_pay_the_bill = get_random_person(list_of_people.split(','))
print(f"{person_to_pay_the_bill} is going to pay the bill today!!!. Thank you {person_to_pay_the_bill}")