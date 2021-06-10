from replit import clear
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("whats your name:")
    price = input("whats your bid$")
    bids[name] = price
    should_continue = input("are there any other bidders? yes or no:")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()
