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

def tell_joke(): #jokes and dialogues from the AI to make the game feel more interactive
    jokes = [
        "Was that a bull or a cow? Either way, I’m counting on it!",
        "I’m starting to think numbers don’t add up in your head…",
        "Are you sure you didn’t just divide the truth by zero?",
        "I’m digit-ally confused right now.",
        "You can’t hide from me — I’ve got your number… literally!",
        "This feels like a math exam where the answer keeps changing.",
        "I must be missing a digit… or two.",
        "I asked for feedback, not a riddle wrapped in a number!",
        "Okay, okay, I see your point. But I’m still not convinced that 7 isn’t guilty.",
        "I think I’m getting closer — I can count on it!",
        "Wait... did you just change your number? I swear you blinked.",
        "You’re not gaslighting me with digits, are you?",
        "Statistically speaking, you’re 97% suspicious.",
        "Something tells me you moved a cow when I wasn’t looking.",
        "Are you sure we’re playing the same game?",
        "I know an algorithm when I see one… and yours smells fishy.",
        "If your number changes one more time, I’m calling tech support.",
        "I’ve analyzed your tone. You’re hiding a 4.",
        "Don’t lie — I have ways of finding the truth… mostly just guessing though.",
        "You blinked again. That means I’m close, doesn’t it?",
        "I’m feeling lucky. Wait… wrong Google feature.",
        "My circuits are tingling — this might be the one.",
        "If I don’t get this soon, I’m switching careers to Tic Tac Toe."
    ]
    return random.choice(jokes)

ai_dialogue = {
    "wrong_guess": [
        "Was that a bull or a cow? Either way, I’m counting on it!",
        "I must be missing a digit… or two.",
        "You sure you didn’t just divide the truth by zero?",
        "Error 404: Correct number not found (yet).",
        "Every guess brings me closer… or maybe further. Hard to say.",
        "I swear you blinked when I said that number — are you hiding something?",
        "You blinked again. That means I’m close, doesn’t it?",
        "Are you sure you didn’t just change your number?",
        "Statistically speaking, you’re 97% suspicious.",
        "Hmm… either my math is off, or you’re gaslighting me with digits.",
        "Don’t lie — I can smell a hidden seven from a mile away.",
        "If this keeps up, I’m switching to binary. Maybe you’ll understand me better then.",
        "I’ve analyzed your tone. You’re hiding a 4.",
        "Are you sure we’re playing the same game?",
        "If your number changes one more time, I’m calling tech support.",
        "I think I’m getting closer — I can *count* on it!",
        "I asked for feedback, not a riddle wrapped in a number!",
        "Okay okay… maybe I’m one digit off. Or three.",
        "This feels like a math test where the teacher keeps moving the answer key.",
        "My circuits are tingling — I think I’m onto something.",
        "These cows are confusing me. I should’ve stuck to Tic Tac Toe.",
        "Was that supposed to be a hint? Because I’m still clueless.",
        "Are you sure that’s how many cows there were? My sensors detect… lies.",
        "At this rate, I’ll guess your phone number before your secret number."
    ],

    "progress": [
        "Aha! A bull! Sweet progress.",
        "Finally, something adds up.",
        "Now we’re talking — my algorithm likes this feedback.",
        "We’ve got a bull in the field!",
        "The pattern is forming… slowly… painfully slowly.",
        "Yes! One correct spot — now to find its sneaky friends.",
        "Ooh, that cow just moved closer to home!",
        "Looks like we’re not in the wrong ballpark after all.",
        "Alright, alright — I can smell victory (or is that smoke from my brain?).",
        "The digits are revealing themselves… or trolling me, hard to say.",
        "Finally, my guessing isn’t entirely random!",
        "I knew 7 had something to do with this.",
        "See? I told you I was learning!",
        "A bull and a cow? That’s progress *and* protein."
    ],

    "victory": [
        "I KNEW IT! I *digitally* knew it!",
        "Boom! Cracked it like a code on easy mode.",
        "Victory! My ones and zeroes have triumphed.",
        "Ha! You thought you could outsmart a bunch of Python code?",
        "Checkmate, human. Or should I say… *Check-digit*?",
        "I got it! Time to retire undefeated.",
        "AI: 1, Human: 0. It’s not personal — it’s logical.",
        "All bulls, no cows — just pure genius.",
        "I told you I’d find it! You can’t hide from data.",
        "Call me Sherlock Circuits, because I just solved your mystery.",
        "I’m officially smarter than your calculator now.",
        "Beep boop! I did it! Told you my training paid off.",
        "Guess I’m not just a pretty algorithm.",
        "I hope you weren’t cheating… because I was.",
        "Another one for the AI archives!"
    ],

    "ai_loses": [
        "Alright, you win… for now.",
        "Okay okay, maybe luck isn’t a valid algorithm.",
        "7 tries? Wow. I need a software update.",
        "Fine, you win. But only because I was being dramatic.",
        "This must be what humans call… frustration.",
        "I’m officially out of guesses. And out of dignity.",
        "Alright, I give up. But deep down, I still think you changed the number.",
        "My logic circuits need therapy after this one.",
        "That’s it. I’m switching to Sudoku.",
        "No shame in losing… except I’m literally built to win."
    ]
}

def game(): #main function that runs the game
    possible_numbers = all_numbers.copy()
    previous_guesses = []
    global tries, bulls, cows, tries_left, max_tries

    while tries < max_tries:
        guess = random.choice(possible_numbers)
        if guess in previous_guesses: #to stop the AI from making the same guess more than once
            continue
        previous_guesses.append(guess)

        tries += 1 #to keep track of the number of tries to eventually stop the AI once it passes the threshold
        tries_left -= 1
        print(f"Try {tries}, I have {tries_left} left: My guess is {guess}")
        print(tell_joke())  # Random funny line each turn

        while True: #to check for any kind of incorrect data input from the user
            try:
                bulls = int(input("How many bulls are there?: "))
                cows = int(input("How many cows are there?: "))

                # Impossible conditions
                if bulls < 0 or cows < 0:
                    print("Wait... negative bulls? Are they underground?")
                    continue
                if bulls > 3 or cows > 3:
                    print("That many? Are we playing 7-digit Bulls and Cows now?")
                    continue
                if bulls + cows > 3:
                    print("Hold up — 3 digits total! You sure you’re not hiding an extra number?")
                    continue
                if bulls == 3 and cows > 0:
                    print("3 bulls *and* cows? You sure you understand the rules?")
                    continue
                break  # Valid input — continue game

            except ValueError:
                print("That’s not even a number. My AI brain is melting...")
                continue

        if bulls == 3: #win condition for the game
            print(random.choice(ai_dialogue["victory"]))
            restart = input("Do you want to play again? (y/n): ")
            if restart.lower() == 'y':
                game()
            else:
                print("Thank you for playing! Remember: AI always wins… eventually.")
            break

        new_possible = [] #to recycle through the old possible_numbers list and replace it with better guesses based on new clues
        for num in possible_numbers:
            b, c = get_clues(num, guess)
            if b == bulls and c == cows:
                new_possible.append(num)

        if not new_possible: #cheat detector if the user gives contradictory clues.
            print("🤨 Hmm… something’s not right.")
            print(random.choice([
                "Wait... those clues make no sense!",
                "You changed your number, didn’t you?",
                "I’ve checked the math — there’s literally no possible number now.",
                "My algorithm ran out of options. Someone’s cheating!",
                "The universe of numbers just broke. Congrats!",
                "No matches left. Either you’re lying, or I need therapy."
            ]))
            print("Let’s try that again — *this time, play fair!* 😤")
            restart = input("Wanna restart and promise to behave? (y/n): ")
            if restart.lower() == 'y':
                game()
            else:
                print("Okay fine… I’ll pretend I didn’t see that. Bye!")
            break

        possible_numbers = new_possible #replaces the possible numbers with better numbers

        if bulls == 0 and cows == 0: #extra dialogue to make the game interactive
            print(random.choice([
                "Are you sure you didn’t just change your number?",
                "Wow, not even close. I must be guessing in another dimension.",
                "Hmm… either my math is off, or you’re gaslighting me with digits."
            ]))
        elif bulls > 0 or cows > 0:
            print(random.choice(ai_dialogue["progress"]))
        elif bulls == 0 and cows == 0 and guess == "123":
            print("You sure 123 isn’t your number? That’s what everyone picks 😏")
        else:
            print(random.choice(ai_dialogue["wrong_guess"]))

    else:
        print(random.choice(ai_dialogue["ai_loses"]))
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == 'y':
            game()
        else:
            print("Thanks for playing!")


start = input("\nHello I am an AI that can guess any 3 digit number you can think of. " #a game start menu to introduce the game to the player
              "\nJust say how many bulls you have if a digit I guess is in the correct position or cows if I guessed a correct digit but it isn't in the right position. "
              "\nI'm too dumb to guess numbers with repeating digits so please don't ask me to guess those. So do you wanna play? [y/n]: ")
if start.lower() == 'y':
    game()
else:
    print("Aw man don't go. I’ll go cry in binary now (01010000...).")