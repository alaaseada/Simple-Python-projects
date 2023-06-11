import random

def guess(x):
    computer_number= random.randint(1, 10)
    user_guess = 0
    while(user_guess != computer_number):
        user_guess = input(f"Guess a number between 1 and {x} or type 'e' to exit: ")
        if user_guess == "e":
            break
        user_guess = int(user_guess)
        if user_guess == computer_number:
            print("Woaaaaaah, your guess is true")
        elif user_guess < computer_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")


def let_computer_guess(x):
    low = 1
    high = x
    match_found = False
    while(not match_found):
        if low == high:
            num = low
        else:
            num = random.randint(low, high)
        user_decision = input(f"Does {num} too high? (h), low?(l), or correct? (c)? (type 'e' to exit) ")
        match user_decision.lower():
            case 'l':
                low = num + 1
            case 'h':
                high = num - 1
            case 'c':
                match_found = True
            case 'e':
                break
            case _:
                print("Invalid input")
    print(f"Yay! the computer found your secret number, {num}")

let_computer_guess(12)
    
