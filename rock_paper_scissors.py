rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

list_images = [rock, paper, scissors]
ia_choise = random.randint(0,2)

while True:
    ia_choise = random.randint(0,2)

    user_choise = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    user_choise = int(user_choise)

    print("You select ")
    print(list_images[user_choise])
    print()
    print("IA select ")
    print(list_images[ia_choise])

    if ia_choise == user_choise:
        print("It's a tie, play again 😊")
        continue

    if user_choise == 0:
        if ia_choise == 1:
            print("You lose 😞")
            break
        else:
            print("You won 😊")
            break
    elif user_choise == 1:
        if ia_choise == 0:
            print("You won 😊")
            break
        else:
            print("You lose 😞")
            break
    elif user_choise == 2:
        if ia_choise == 1:
            print("You won 😊")
            break
        else:
            print("You lose 😞")
            break