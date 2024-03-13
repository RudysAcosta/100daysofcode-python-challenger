from art import logo

bidders = []

def main():
    print("Welcome to the secret auction program. ")
    bidder = 'yes'
    while bidder == 'yes':
        get_bidder_details()
        bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")

    print(bidders)
    print("______")
    print(get_winner())

def get_winner():
    winner = bidders[0]
    for bidder in range(1, len(bidders)):
        if winner['bid'] < bidder['bid']:
            winner = bidder
    return winner

def get_bidder_details():
    name = input("What is your name?:  ")
    bid = float(input("What's your bid?:  "))
    bidder = { 'name': name, 'bid': bid }
    bidders.append(bidder)

if __name__ == "__main__":
    main()