#creating a game Rock paper sissors
from random import choices # importing random modules
import sys
while True:
    # user input
    while True:
        user_input=list(input("Enter 'r' for rock,'p' for paper,'s' for sissors: "))
        if "r" in user_input:
            break
        elif "p" in user_input:
            break
        elif "s" in user_input:
            break
        else:
            print('invalid choice !!,choose from "r","p" or "s"')
            continue
        ##
    choice=['r','p','s']
    random_choice=choices(choice)
    print(f"your choice is{user_input}")
    print(f"computer choice is {random_choice}")
        # win or tie situation
    def game():
        tie()
        win()
    def tie():
        if random_choice == user_input:
            print("The game is tie")
            return
    def win():
        # r>s,s>p,p>r
        if 'r' in random_choice and 'p' in user_input:
            print("you won")
        elif 'r' in random_choice and 's' in user_input:
            print("you lost")
        elif 'p' in random_choice and 'r' in user_input:
            print("you lost")
        elif 'p' in random_choice and 's' in user_input:
            print("you won")
        elif 's' in random_choice and 'r' in user_input:
            print("you won")
        elif 's' in random_choice and 'p' in user_input:
            print("you lost")
            return
    game()
    while True:
        cont=input("For continue press (Y) and For exit press (N): ")
        if cont=="Y":
            break
        elif cont=="N":
            sys.exit()
        else:
            print("choose from 'Y' or 'N' ")
            continue