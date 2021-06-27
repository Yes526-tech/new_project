#Display art.

#Generate a random account from the game data.

#Format the account data into printable format

#Ask user for a guess.

#Check if user is correct.
##Get follower count of each account.
##Use if statement to check if user is correct.

#Give user feedback on their guess.

#Score keeping.

#Make the game repeatable.

#Making account at position become the next account at possible.

#Clear the screen between rounds.

from game_data import data
import random
score = 0


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")
    guess = input("who has more followers? Type 'A' or 'B':").lower()


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"you're right! Current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score : {score}.")


