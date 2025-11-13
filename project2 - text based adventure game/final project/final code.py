# initializing
from random import randint

# chapter lists
# structure: prompt, options, correct answers, hint, success messaage, failure adjective
yourHouse = ["You were woken up by the sound of pecking outside your window. An owl with an old scroll flew in. Do you",
     ["a. reward him your breakfast", "b. cruelly shoo him away", "c. scream for help"],
     ["a", "A"],
     ["Hint: The owl is hungry"],
     ["The owl was very happy with your food."],
     ["cowardice"]
     ]

forkPathway = ["You follow the owl to a fork pathway. Do you",
     ["a. go right towards the forest", "b. go left towards the ocean", "c. go straight to the cave"],
     ["a", "A", "b", "B"],
     ["Hint: The owl is scared of the dark."],
     ["Owl: And you live another day :()"],
     ["ignorant"]
    ]

pathway = ["The sky is getting dark, suddenly a werewolf jumps out baring its fangs. Do you",
     ["a. scream and runaway", "b. stand tall and fight him", "c. hide and look for a weapon"],
     ["c", "C"],
     ["Hint: This might help you later on"],
     ["You and wise owl quickly hid behind a tree, hoping he didn't see you."],
     ["stupid"]
     ]

behindTree = ["Here, you found a magical branch aka wand. Do you",
     ["a. jump out and stab the werewolf", "b. turn yourself into a frog and hope he won't see you", "c. look to wise owl for help",],
     ["b", "B"],
     ["Hint: don't try fighting him"],
     ["Luckily, the werewolf forgot his glasses so you sneakily hopped away."],
     ["weak"]
     ]
chest = ["You arrive at a chest, you can only pick one thing to help you later on. Do you choose",
     ["a. lunch", "b. book of spells", "c. healing potion"],
     ["a", "A"],
     ["Hint: Befriend the owl"],
     ["You and wise owl bonded over a shared lunch."],
     ["selfish"]
     ]
castleFire = ["You arrive at the castle the princess is stuck at. Suddenly a magical fire comes roaring towards you. Do you",
     ["a. try to remember a spell that works", "b. wait for it to burn out", "c. throw up your lunch",],
     ["c", "C"],
     ["Hint: You ate too much at lunch"],
     ["Disgusting, the fire was extinguished by your vomit."],
     ["brainless"]
     ]
finalDuel = ["You continue on and meet the evil witch. You guys have a final duel. Do you",
     ["a. use your wits", "b. use your wand", "c. hide"],
     ["c", "C"],
     ["Hint: You're still a frog"],
     ["Congradulations, you survived and saved the princess!"],
     ["useless"]
     ]

chapterList = [yourHouse, forkPathway, pathway, behindTree, chest, castleFire, finalDuel]

# variables
linebreak = "──────────────────────────────────────── ୨୧ ────────────────────────────────────────"
hearts = 9 # beginning hearts
maxTries = 2 # max number of tries per chapter

# defining functions

# define instruction function
def instruction(name):
    print(f"{linebreak}\nHello {name}! You have entered into a magical world where your lifespan depends on each choice you make.\nYou start with nine lives, and after each choice you'll find out if that cost you a heart or two.\nYour goal is to survive until the end.\nAnd if you run out, well, you know what happens, good luck!\n{linebreak} ")
    return

# define letter function
def letter(name):
    print(f"You open the scroll: \nDear {name}, we just got word that the royal princess has been captured by the evil witch! She needs your help to save her, follow the owl and you'll succeed!\nWish you the best,\nAnonymous,")
    return

# define check answer function
def checkAnswer(chapter_data):
    global hearts
    
    # asking for answer
    userAnswer = input().strip()
    
    correct_answers = chapter_data[2]

    if userAnswer in correct_answers:
        print(chapter_data[4]) # success message
        hearts += randint(1, 3) # hearts reward
        print(f"Success! You now have {hearts} hearts")
        return True
    else:
        print(owlResult(chapter_data[5])) # failure message
        hearts -= randint(1, 3) # hearts deduct
        print(f"You now have {hearts} hearts")
        return False

# define chapter function - if player survived chapter and if they should move on
def chapter(chapter_data):
    global hearts
    print(linebreak)
    print(chapter_data[0]) # prints prompt

    for choice in chapter_data[1]:
        print(choice) # prints choices

    tries = 0
    while tries < maxTries:
        if checkAnswer(chapter_data):
            return True # if answer correct, move on
        
        if hearts <= 0:
            return False # if no more hearts, player dies
        
        tries += 1

        # hint on second try only
        if tries == 1:
            print(f"Try again! ({maxTries - tries} attempt left).")
            print(f"{chapter_data[3][0]}") # hint

    # if no more tries but player is still alive
    print("You ran out of tries. You barely managed to escape with wise owl's help but you lose one heart due to your poor decisions.")
    hearts -= 1
    print(f"You now have {hearts} hearts.")
    return True

# define owl result function
def owlResult(adjective):
    print(f"The wise owl deemed you {adjective}, and pecked you to death.")
    return

# define game loop function
def gameLoop(chapters, name):
    global hearts
    chapter_count = 0

    for current_chapter in chapters:
        chapter_count += 1

        # printing letter after first chapter
        if chapter_count == 2:
            letter(name)

        player_survived_chapter = chapter(current_chapter)

        # if player ran out of hearts
        if not player_survived_chapter: #or hearts <= 0
            print("GAME OVER\nYou ran out of hearts, the witch wins and our dearest owl is most disapointed in you!")
            return
        
    # if player successful
    print(f"{linebreak}\nCONGRADULATIONS {name}! You survived and saved the princess from the evil witch (with the owl's help of course)!")
    return


# main game program

# asking for name
name = input("Hello Adventurer, what is your name?").strip()

# printing instructions
(instruction(name))

# main game loop function
gameLoop(chapterList, name)
