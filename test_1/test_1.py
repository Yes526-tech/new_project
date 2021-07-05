#test making hangman
import random

words = ["apple", "banana", "cheery", "peach", "pomegranate", "apricot", "kiwi"]
selected = random.choice(words)
print(selected)
new_word = []
for _ in range(len(selected)):
    new_word.append("_")
print(new_word)
live = 5

choice = input("guess a letter> ").lower()
if choice in selected:
    new_word.remove(selected.index(choice))
# if choice in selected:
#     print("correct")
#
# else:
#     print("wrong")
#     live -= 1
#     print(live)