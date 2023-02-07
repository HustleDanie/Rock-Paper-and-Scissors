import random

print("Welcome to Rock, Paper, Scissors game!")

while True:
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print("User has chosen: " + choice_name)
    print("Now its computer turn.......")

    comp_choice = int(3 * (random.random())) + 1

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer has chosen: " + comp_choice_name)

    print(choice_name + " V/S " + comp_choice_name)

    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("Paper wins => ", end="")
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
         (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("Scissors wins =>", end="")
        result = "Scissors"

    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
