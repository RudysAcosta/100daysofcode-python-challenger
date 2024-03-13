import random
import os
from image_asii import hangman_states, banner

word_list = [
    "python", "java", "javascript", "ruby", "perl", 
    "swift", "csharp", "cplusplus", "html", "css", 
    "react", "angular", "vue", "django", "flask", 
    "spring", "dotnet", "docker", "kubernetes", "devops", 
    "cloud", "aws", "azure", "gcp", "linux", 
    "windows", "macos", "ubuntu", "debian", "fedora"
]

selected_word = random.choice(word_list)
guessed_characters = []
killer = 0
end_of_game = False

print(banner)
print(' _ ' * len(selected_word))
print()

def get_guess_char():
    word = []
    for char in selected_word:
        if char in guessed_characters:
             word.append(char)
        else:
            word.append('_')
    return word

def display_handman():
    print(hangman_states[killer])

def check_win():
    return ''.join(get_guess_char()) == selected_word

while not end_of_game:
    os.system('cls' if os.name == 'nt' else 'clear')
    display_handman()

    if len(guessed_characters) > 0:
       print(' '.join(get_guess_char())) 

    if check_win():
        print("You won")
        end_of_game = True

    if killer == 6:
        print('Game over')
        end_of_game = True
    
    choice = input("Please guess a letter: ")

    if choice in guessed_characters:
        print("Letter guessed")
        continue

    if choice in selected_word:
        guessed_characters.append(choice)
    else:
        killer += 1