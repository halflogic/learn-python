# A game of rock, paper, scissors against the computer

import sys
import random

print("Welcome to Rock, Paper, Scissors game!")
win = 0
lose = 0
tie = 0

# use dictionary for the choices
choice_dict = {'r':'Rock', 'p':'Paper', 's':'Scissors'}


while True:
    print("-----------------------------")
    print("Score: Win=" + str(win) + " Lose=" + str(lose) + " Tie=" + str(tie))
    print("-----------------------------")
    print("\nSelect (r) for Rock, (p) for Paper, (s) for Scissors or (q) to quit the game.")
    player_choice = input("Enter your choice: ")
    
    if player_choice == 'q':
        print("Exiting game. Thank you for playing!")
        sys.exit()
    
    elif player_choice == 'r' or player_choice == 'p' or player_choice == 's':
        print("You chose: ", choice_dict[player_choice])
        
        # Generate random choice for computer
        computer_choice = random.choice(list(choice_dict.keys()))
        print("Computer chose: ", choice_dict[computer_choice] )
        print(">> " + choice_dict[player_choice] + " -vs- " + choice_dict[computer_choice]) 

        # Check who wins and tally score
        if player_choice == computer_choice:
            tie += 1
            print(">> It's a tie!")
        elif player_choice == 'r' and computer_choice == 's':
            win += 1
            print(">> You win!")
        elif player_choice == 'p' and computer_choice == 'r':
            win += 1
            print(">> You win!")
        elif player_choice == 's' and computer_choice == 'p':
            win += 1
            print(">> You win!")
        elif player_choice == 'r' and computer_choice == 'p':
            lose += 1
            print(">> You lose!")
        elif player_choice == 'p' and computer_choice == 's':
            lose += 1
            print(">> You lose!")
        elif player_choice == 's' and computer_choice == 'r':
            lose += 1
            print(">> You lose!")
        else:
            print(">> Undetermined result <<")


    else:
        print(">> Invalid selection! Try again.")