import random
print("Welcome to the Number Guessing Game!")
selected_num = []


def guess_num(number):

    numbers_list = []

    for number in range(1, 101):
        numbers_list.append(number)

    selected_number = random.choice(numbers_list)
    selected_num.append(selected_number)
    print(f"shh number is {selected_number}")
live = 5
guessing = True
guess_num(number=selected_num)

while guessing:
    guess_number = []
    guess = int(input("guess number>"))
    guess_number.append(guess)
    if guess_number == selected_num:
        guessing = False

        print("you guessed correct")
    else:
        print("you guessed wrong")
        live -= 1
        print(f"lives: {live}")
        hint = input("hint?: 'y' or 'n'> ")
        if hint == "y":
            if guess_number > [50] and selected_num < [50]:
                print("you too high")
            elif guess_number < [50] and selected_num > [50]:
                print("you too low")
            elif guess_number == [50] and selected_num < [50]:
                print("down")
            elif guess_number == [50] and selected_num > [50]:
                print("up")

        if live == 0:
            print("you out of your lives")
            guessing = False



