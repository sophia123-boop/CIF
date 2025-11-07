linebreak = "──────────────────────────────────────── ୨୧ ────────────────────────────────────────"

# define instruction function
def instruction(name):
    return print(f"{linebreak}\nHello {name}! You have entered into a magical world where your lifespan depends on each choice you make.\nYou start with nine lives, and after each choice you'll find out if that cost you a heart or two.\nYour goal is to survive until the end.\nAnd if you run out, well, you know what happens, good luck!\n{linebreak} ")

name = input("Hello Adventure, what is your name?")

# printing instructions
instruction(name)