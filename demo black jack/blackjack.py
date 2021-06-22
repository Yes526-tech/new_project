# import random
# gamer_cards = []
# dealer_cards = []
#
# letter_cards_value = {
# "J": 10,
# "Q": 10,
# "K": 10,
# "A": 10
# }
# def deal_card():
#     cards = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
#     return random.choice(cards)
# for _ in range(2):
#     gamer_cards.append(deal_card())
#     dealer_cards.append(deal_card())
#
# def calculate_gamer(gamer_card):
#     if "J" in gamer_cards:
#         gamer_cards.remove("J")
#         gamer_cards.append(letter_cards_value["J"])
#         print(sum(gamer_cards))
#
#     elif "Q" in gamer_cards:
#         gamer_cards.remove("Q")
#         gamer_cards.append(letter_cards_value["Q"])
#         print(sum(gamer_cards))
#
#     elif "K" in gamer_cards:
#         gamer_cards.remove("K")
#         gamer_cards.append(letter_cards_value["K"])
#         print(sum(gamer_cards))
#
#     elif "A" in gamer_cards:
#         gamer_cards.remove("A")
#         gamer_cards.append(letter_cards_value["A"])
#         print(sum(gamer_cards))
#
# def calculate_dealer(dealer_card):
#     if "J" in dealer_cards:
#         dealer_cards.remove("J")
#         dealer_cards.append(letter_cards_value["J"])
#         print(sum(dealer_cards))
#
#     elif "Q" in dealer_cards:
#         dealer_cards.remove("Q")
#         dealer_cards.append(letter_cards_value["Q"])
#         print(sum(dealer_cards))
#
#     elif "K" in dealer_cards:
#         dealer_cards.remove("K")
#         dealer_cards.append(letter_cards_value["K"])
#         print(sum(dealer_cards))
#
#     elif "A" in dealer_cards:
#         dealer_cards.remove("A")
#         dealer_cards.append(letter_cards_value["A"])
#         print(sum(dealer_cards))
# print(f"your cards: {gamer_cards}, your point = {calculate_gamer}")
# print(f"dealer cards: {dealer_cards}, dealer point = {calculate_dealer}" )
# # def compare(card):
#
list_1 = ["J"]
dict_1 = {
"J": 10
}
if "J" in list_1:
    list_1.remove("J")
    list_1.append(list_1(10))
print(list_1)