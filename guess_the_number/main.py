import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

number = random.randint(1, 100)

def run():
    attempts = 0
    display_welcome_message()

    difficulty = get_difficulty()

    if difficulty == 'hard':
        attempts = EASY_LEVEL_TURNS
    else:
        attempts = HARD_LEVEL_TURNS

    while attempts > 0:
        messeger_attempts(attempts)
        guess_number = to_play()

        comparation = compare_numbers(guess_number)

        if comparation == 'win':
            print(f"You got it! The answer was {guess_number}")
            exit()
        else:
            print(f"Too {comparation}.")
            attempts -= 1

    print("You lose.")


def get_difficulty():
    return input("Choose a difficulty. Type 'easy' or 'hard': ")

def display_welcome_message():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

def messeger_attempts(attempts):
    print(f"You have {attempts} remaining to guess the number.")

def to_play():
    return int(input("Make a guess: "))

def compare_numbers(guess_number):
    global number

    if number > guess_number:
        return 'low'
    elif number < guess_number:
        return 'high'
    
    return 'win'

if __name__ == '__main__':
    run()