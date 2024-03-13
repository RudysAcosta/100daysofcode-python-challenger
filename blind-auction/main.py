import os
from art import logo

bidders = []

def main():
    print(logo)
    print("Welcome to the secret auction program. ")
    while True:
        get_bidder_details()
        while True:
            bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
            if bidder not in ['no', 'yes']:
                print("Invalid input. Please try again.")
                continue
            if bidder == 'yes':
                break
            if bidder == 'no':
                winner = get_winner()
                print(f"The winner is {winner['name'].capitalize()} with a bid of ${winner['bid']}")
                exit()
            
def get_winner():
    return max(bidders, key=lambda bidder: bidder['bid'])

def get_bidder_details():
    name = input("What is your name?:  ")
    bid = float(input("What's your bid?:  "))
    bidder = { 'name': name, 'bid': bid }
    bidders.append(bidder)
    os.system("clear")

if __name__ == "__main__":
    main()