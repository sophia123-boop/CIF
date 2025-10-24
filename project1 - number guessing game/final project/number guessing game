# importing the randint function
from random import randint

# introducing game
print("- welcome to the number guessing game -\n tip: at any point, type x to quit ")

# setting up while loop if user wants to start new round
new_round = "y"
while new_round == "y":

    # setting boundaries
    while True:
        try:
            # asking user to input a range
            low = int(input("enter a lower boundary"))
            high = int(input("enter an upper boundary"))
        
            # checking if range makes sense
            if low >= high:
                print("make sure first number is lower")
            else:
                break
        
        except ValueError:
            print("both inputs have to be integers")

    # setting limit trials
    trials = None
    while True:
        input_trials = input("would you like to limit trials")
        if input_trials == "y":
            try:
                is_limited = True
                trials = int(input("how many tries do you think you'll get it in"))
                tries_left = trials
                if trials > 0:
                    break
                else:
                    print("make sure tries is a positive integer")
            except ValueError:
                print("make sure tries is an integer")
        elif input_trials == "n":
            is_limited = False
            break
        else:
            print("please enter y/n")

    # setting up
    # generate a random number between user input boundary
    random_num = randint(low, high)
    print("- starting new round -")
    guessed = 0
    game_won = False
    end_game = False

    # main guessing loop
    while not game_won and not end_game:

        if game_won or end_game:
            break
        
        # guessing loop
        while is_limited == True and guessed < trials:
            if input_trials == "y":
                is_limited = True
                # ask user to input guess
                guess_num = input(f"guess a number between {low} and {high} (inclusive) you have {tries_left} tries left: ")
            
            try:
                guess_num = int(guess_num)
            
                # check if matched
                if random_num == guess_num:
                    print("- correct, you won -")
                    game_won = True
                    break
                else:
                    if guess_num < random_num:
                        print("too small") 
                    else:
                        print("too big")
            except ValueError:
                print("please enter integers only or x to quit")

            while guessed < trials and input_trials == "y" and is_limited == True:
            # adding to guess
                guessed += 1
                tries_left = trials - guessed
                break

        while is_limited == False:
            if input_trials == "n":
                # ask user to input guess
                guess_num = input(f"guess a number between {low} and {high} (inclusive):")

            try:
                guess_num = int(guess_num)
            
                # check if matched
                if random_num == guess_num:
                    print("- correct, you won -")
                    game_won = True
                    break
                else:
                    if guess_num < random_num:
                        print("too small") 
                    else:
                        print("too big")
            except ValueError:
                print("please enter integers only or x to quit")

        # if user enters x break loop
        if guess_num == "x":
            print("- ending current round -")
            end_game = True
            break

                    
            
        if guessed == trials and not game_won and is_limited == True:
            end_game = True
            print("- you ran out of tries -")

        if new_round != "y":
            rate = int(input("thank you for playing please rate us out of five (enter number 1-5)"))
            break

# printing correct number
    if not game_won:
        print("the correct number was", random_num)
    int(input("thank you for playing please rate us out of five (enter number 1-5)"))

    # asking if they want to play another round
    new_round = input("would you like to play another round")
    if new_round == "n":
        print("bye, have a nice day")
        break
