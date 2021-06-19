
def check_odd_or_even(number):
    """
    This function accepts an input parameter and checks if it's even or odd
    :param number(int):
    :return: None
    """
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

number = int(input("Enter a number: "))
check_odd_or_even(number)
