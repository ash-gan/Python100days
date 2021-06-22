
def find_treasure():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    game_over = True
    while game_over:
        choice1 = input("You\'r at a cross road.Do you want to left or right? \n" ).lower()
        if choice1 == "right":
            print("Game Over, try again!!!")
        elif choice1.lower() == "left":
            choice2 = input("You have come to a lake. There is an island in the middle of the lake. " \
                            "Type 'wait' to wait for a boat or 'swim' to swim across."
                            "Do you want to swim or wait? ").lower()
            if choice2 == "swim":
                print("Game Over, try again!!!")
            elif choice2 == "wait":
                choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. /"
                                "One red, one yellow and one blue. \
                                Which color door you would like to open ?").lower()
                if choice3 == "red":
                    print("It\'s a room full of fire. Game Over, try again!!!")
                elif choice3 == "blue":
                    print("You enter a room of beasts. Game Over, try again!!!")
                elif choice3 == "yellow":
                    print("You found the treasure. You Win!!!")
                    game_over = False
                else:
                    print("Valid inputs are red, blue or yellow. Try again!!!")
            else:
                print("Valid inputs are Swim or Wait.")
        else:
            print("Valid inputs are left or right, please try again later.")


print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________ ________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
find_treasure()






