import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create a list of characters (letters, symbols, numbers) and a list of choices (number of letters, symbols, numbers)
list_chat = [letters, symbols, numbers]
list_choise = [nr_letters, nr_symbols, nr_numbers]

password = ""

# While there are still characters to be added to the password
while list_choise.count(0) != 3:
    # Randomly select a type of character (letter, symbol, number)
    random_choise = random.randint(0, 2)

    # If the user has requested 0 of this type of character, skip to the next iteration
    if list_choise[random_choise] == 0:
        continue

    # Select a character of the chosen type and add it to the password
    chart = list_chat[random_choise]

    password += chart[random.randint(0, len(chart) - 1)]
    list_choise[random_choise] -= 1

print(password)