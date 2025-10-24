# importing the randint function
from random import randint

# generate a random number between 0 to 100
random_num = randint(0, 100)

# ask user to input guess
guess_num = int(input("Guess a number between 0 and 100 (inclusive)"))

# check if matched
if random_num == guess_num:
    print("you won")
else:
    print("you lost")