import random
from itertools import permutations

all_numbers = [''.join(p) for p in permutations('0123456789', 3) #creates random 3-digit numbers and removes numbers with its front digit being 0
               if p[0] != '0']

def game():
    victory = False
    while victory == False: #simple while loop system to keep the AI guessing
        guess = random.choice(all_numbers)
        print("My guess is", guess)
        bulls = int(input("How many bulls are there?: "))
        cows = int(input("How many cows are there?: "))
        if bulls == 3: #win condition for the game
            victory = True
            print("I win!")
            restart = input("Do you want to restart? (y/n): ")
            if restart.lower() == 'y':
                game()
            else:
                print("Thanks for playing!")
        else:
            victory = False
            guess = random.choice(all_numbers)
            print("My guess is", guess)
            bulls = int(input("How many bulls are there?: "))
            cows = int(input("How many cows are there?: "))

game()