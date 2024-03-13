from art import logo

bidders = []

def main():
    print("Welcome to the secret auction program. ")
    bidder = 'yes'
    while bidder == 'yes':
        get_bidder_details()
        bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")

    winner = get_winner()
    print(f"The winner is {winner['name'].capitalize()} with a bid of ${winner['bid']}")
    print()

def get_winner():
    return max(bidders, key=lambda bidder: bidder['bid'])

def get_bidder_details():
    name = input("What is your name?:  ")
    bid = float(input("What's your bid?:  "))
    bidder = { 'name': name, 'bid': bid }
    bidders.append(bidder)

if __name__ == "__main__":
    main()