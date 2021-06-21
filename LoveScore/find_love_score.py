
def find_love_score(name1, name2):
    first_position_total = 0
    second_position_total = 0
    final_string = name1.lower()+name2.lower()
    magic_string="truelove"
    for i in range(0,len(magic_string)):
        cnt = final_string.count(magic_string[i])
        if i < 4:
            first_position_total+=cnt
        else:
            second_position_total+=cnt
    return str(first_position_total)+str(second_position_total)

your_name = input("Enter your name: ")
partner_name = input("Enter your partner name: ")
love_score = int(find_love_score(your_name, partner_name))

if   10 > love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos!")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alight together")
else:
    print(f"Your score is {love_score}")










