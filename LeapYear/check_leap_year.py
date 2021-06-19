
def check_if_leap_year(year_input):
    if year_input%4 == 0:
        if year_input % 100 ==0:
            if year_input % 400 == 0:
                print(f"{year_input} Year is leap year")
            else:
                print(f"{year_input} Year is not leap year")
        else:
            print(f"{year_input} Year is leap year")
    else:
        print(f"{year_input} Year is not leap year")

input_year= int(input("Enter the year: "))
check_if_leap_year(year_input=input_year)

