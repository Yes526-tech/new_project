winner_is_known = False


while not winner_is_known:
    bids = {}

    name_user = input("whats your name?: ")
    user_bid = int(input("whats your bid?: "))

    bids[name_user] = user_bid
    choice = input("continue or sell 'y' or 'n': ")
    if choice == "n":
        winner_is_known = True
        max_paid_bill = max(bids[max_bid] for max_bid in bids)
        for name in bids.keys():
            if bids[name] == max_paid_bill:
                print("the winner is " + name)





















