import random

# J, Q, K = 11 and A = 1 or 11 
maso = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

your_cards = []
ia_cards = []

def add_card(lotter, card):
    lotter.append(card)

def get_card_with_maso(ia = False) -> int:
    index = random.randint(0, len(maso) - 1)
    return maso.pop(index)

def check_cards(cards):
    total = sum(cards)

    # if A is on lotter, and de total more than 21
    # aqui hay que tomar otro algorigmo en el futuro por si el lotte 
    # tienen mas de una A
    if 11 in cards and total > 21:
        index = cards.index(11)
        cards[index] = 1
        total = sum(cards)

    return total

def show_cards(all = False):
    print(f"Your cards: {your_cards}, current score: {check_cards(your_cards)}")
    if all:
        print(f"Cumputer's cards: {ia_cards}, current score: {check_cards(ia_cards)}")
    else:
        print(f"Cumputer's first card: {ia_cards[0]}")

def any_one_lose():
    if check_cards(your_cards) > 21:
        return 0
    elif check_cards(ia_cards) > 21:
        print("La ia perdites")
        return 1
    return -1

def check_win():
    you_score = check_cards(your_cards)
    ia_score = check_cards(ia_cards)

    if you_score > 21:
        return -1
    
    if ia_score > 21:
        return 0

    if you_score == ia_score:
        return 1
    elif you_score > ia_score:
        return 0
    else:
        return -1


def ia_continue_game():
    """
    wen the user ser no more card, de ia continue play
    """
    while check_cards(ia_cards) < 17:
        add_card(ia_cards, get_card_with_maso())

def show_final(msg = "Stalemate at the table! Both players have the same score in this hand"):
    show_cards(True)
    print(msg)

is_start =  input("Do you want to play a game of Backjack? Type 'y' or 'n':  ")

if is_start == 'y':
    
    while True:
        add_card(your_cards, get_card_with_maso())
        if check_cards(ia_cards) < 17:
            add_card(ia_cards, get_card_with_maso())

        lose = any_one_lose()

        if lose == 0:
            show_final("You went over, You lose 😭")
            exit()
        elif lose == 1:
            show_final("Hey You, the ia want more an then you win 🤪")
            exit()

        show_cards()
    
        get_another = input("Type 'y' to get another card, type 'n to pass:'")
        
        if get_another == 'y':
            continue
        else:
            ia_continue_game()
            win = check_win()

            if win == 1:
                show_final()
            elif win == 0:
                show_final("You went over, You you win 🤪")
            else:
                show_final("You went over, You lose 😭")
            
            exit()
else:
    print("Bye!!!")
    exit()