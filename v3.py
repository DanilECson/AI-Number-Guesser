import random
from itertools import permutations

all_numbers = [''.join(p) for p in permutations('0123456789', 3) #creates random 3-digit numbers and removes numbers with its front digit being 0
               if p[0] != '0']

def get_clues(secret, guess): #is used to calculate how many cows and bulls there are and their positions
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

tries = 0
tries_left = 7
max_tries = 7 #the AI gets a maximum of seven tries to guess the number

def game(): #main function that runs the game
    possible_numbers = all_numbers.copy()
    previous_guesses = []
    global tries, bulls, cows, max_tries, tries_left

    while tries < max_tries:
        guess = random.choice(possible_numbers)
        if guess in previous_guesses:  # to stop the AI from making the same guess more than once
            continue
        previous_guesses.append(guess)

        tries += 1  # to keep track of the number of tries
        tries_left -= 1
        print(f"Try {tries}, I have {tries_left} left: My guess is {guess}")
        bulls = int(input("How many bulls are there?: "))
        cows = int(input("How many cows are there?: "))

        if bulls == 3: #win condition for the game
            print("I win!")
            restart = input("Do you want to play again? (y/n): ")
            if restart.lower() == 'y':
                game()
            else:
                print("Thank you for playing!")
            break

        new_possible = [] #to recycle through the old possible_numbers list and replace it with better guesses based on new clues
        for num in possible_numbers:
            b, c = get_clues(num, guess)
            if b == bulls and c == cows:
                new_possible.append(num)

        possible_numbers = new_possible  # replaces the possible numbers with better numbers

    else:
        print("I couldn't guess it!")
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == 'y':
            game()
        else:
            print("Thanks for playing!")

game()