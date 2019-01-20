import time
import random
from sys import exit


def print_pause(message):
    print(message)
    time.sleep(1)


def introduction():
    print_pause("Welcome to the Castle of Doom game")
    print_pause(
        "For years, a powerful wizard "
        "has been terrorizing a nearby land.")
    print_pause(
        "As a hero travelling this land, "
        "you feel tempted to do something about it.")
    print_pause(
        "In this game, your choices will "
        "either lead to victory or an untimely death.")
    print_pause("Have fun!")


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if option in response:
                return response
        print_pause("Please write a valid number.")


def game_over():
    print_pause("Your adventure ended....")
    response = valid_input("Would you like to play again\n"
                           "1 - Yes\n"
                           "2 - No\n", ["1", "2"])
    if response == "1":
        start_game()
    else:
        print_pause("It was fun having you around. "
                    "Try again later.")
        exit(0)


def first_floor(inventory):
    print_pause("This is the lava floor "
                "of the castle.")
    if "silvershield" in inventory:
        print_pause("There is nothing else to do here. "
                    "Choose other floor.")
        walk_stairs(inventory)
    else:
        print_pause(
            "No matter where you look, lava fills the room "
            "apart from a small platform in the center with a shield.")
        print_pause(
            "You may try to jump to get to the shield "
            "but chances are not on your side.")
        response = valid_input("What will you do?\n"
                               "1 - Try to jump.\n"
                               "2 - Turn back.\n", ['1', '2'])
        if response == '1':
            print_pause("You try to jump to the central platform.")
            if 'flyingboots' in inventory:
                print_pause(
                    "Luckily you already go the flying boots. "
                    "This will be easy.")
                print_pause(
                    "You managed to land in the central platform "
                    "and got the silver shield.")
                inventory.append("silvershield")
                print_pause("You turn back towards the stairs.")
                walk_stairs(inventory)
            else:
                print_pause("This will require a lucky jump.")
                choices = ["Lucky", "Not Lucky"]
                if random.choice(choices) == "Lucky":
                    print_pause(
                        "Not knowing how, you managed to land in "
                        "the central platform and got the silver shield.")
                    inventory.append("silvershield")
                    print_pause("You turn back towards the stairs.")
                    walk_stairs(inventory)
                else:
                    print_pause(
                        "During the jump, your feet slipped up "
                        "and you landed in the lava. "
                        "Ouch, this probably hurt a lot!")
                    game_over()
        else:
            print_pause("You turn back towards the stairs.")
            walk_stairs(inventory)



def second_floor(inventory):
    print_pause("Welcome to the random sanctuary.")
    if "flyingboots" in inventory:
        print_pause("There is nothing else to do here. Choose other floor.")
        walk_stairs(inventory)
    else:
        print_pause(
            "As you walk inside, you see a message glowing in the wall.")
        print_pause("This is the most unfair place in the whole castle.")
        print_pause(
            "Inside the chest is either a bomb or an useful item.")
        print_pause(
            "If you open it, you will either get an useful item "
            "or you will die.")
        print_pause("I would turn back if I was in your place.")
        print_pause("Signed - The wizard.")
        response = valid_input("What will you do?\n"
                               "1 - Open the chest.\n"
                               "2 - Turn back.\n", ["1", "2"])
        if response == "1":
            print_pause("Despite the warnings, you try to open "
                        "the chest and...")
            choices = ["Lucky", "Not Lucky"]
            if random.choice(choices) == "Lucky":
                print_pause("Thankfully it did not explode.")
                print_pause("Inside there were some flying boots.")
                inventory.append("flyingboots")
                print_pause("You return to the stairs.")
                walk_stairs(inventory)
            else:
                if "silvershield" in inventory:
                    print_pause(
                        "There is a bomb which exploded in your face.")
                    print_pause(
                        "Luckily your silver shield protected you "
                        "from the impact.")
                    print_pause("You return to the stairs empty-handed.")
                    walk_stairs(inventory)
                else:
                    print_pause(
                        "There is a bomb which exploded in your face.")
                    game_over()
        else:
            print_pause("You turn back towards the stairs.")
            walk_stairs(inventory)


def third_floor(inventory):
    print_pause("Welcome to the cuddly floor of the castle.")
    if "goldensword" in inventory:
        print_pause("There is nothing else to do here. Choose other floor.")
        walk_stairs(inventory)
    else:
        print_pause("Home to the legion of murderous cats of the wizard.")
        print_pause(
            "There is a sofa near the sleeping cats "
            "where a golden sword sparkles.")
        print_pause(
            "You can try to get to it but if the cats wake up, "
            "you are probably going to die.")
        response = valid_input("What will you do?\n"
                               "1 - Try to get the sword.\n"
                               "2 - Turn back.\n", ["1", "2"])
        if response == "1":
            if "flyingboots" in inventory:
                print_pause(
                    "Oh wait, you already have the flying boots. "
                    "This will be such an anti-climax.")
                print_pause(
                    "You fly above the cats, get into the sofa "
                    "and easily get the golden sword.")
                inventory.append("goldensword")
                print_pause("You return to the stairs.")
                walk_stairs(inventory)
            else:
                print_pause(
                    "You try to tiptoe quietly around the sleeping cats.")
                choices = ["Lucky", "Not Lucky"]
                if random.choice(choices) == "Lucky":
                    print_pause(
                        "Thankfully you managed not to "
                        "wake up the sleeping cats.")
                    print_pause("You grab the golden sword from the sofa.")
                    print_pause(
                        "And promptly make your way back to the stairs.")
                    inventory.append("goldensword")
                    walk_stairs(inventory)
                else:
                    print_pause("Unfortunately you snap a little twig.")
                    print_pause(
                        "The cats wake up and start looking "
                        "at you with cuddly eyes.")
                    print_pause(
                        "You try to fight back the feeling "
                        "but unfortunately they are too strong.")
                    print_pause(
                        "You are condemned to an eternity in the castle "
                        "as a slave to the cats.")
                    game_over()
        else:
            print_pause("You turn back towards the stairs.")
            walk_stairs(inventory)


def fourth_floor(inventory):
    print_pause("This is the den of the wizard.")
    print_pause("Like a normal villain, he looks at you and starts gloating.")
    print_pause(
        "After his talk on ruling the world, he conjures a fireball.")
    if "silvershield" in inventory:
        print_pause("You use your shield to deflect his spell. Good job!")
    else:
        print_pause(
            "You have no defense method and end up "
            "completely charred by the spell.")
        print_pause(
            "What were you expecting fighting "
            "the final boss at the beginning?")
        game_over()
    print_pause("Now is your turn to attack!")
    if "goldensword" in inventory:
        print_pause("Your magical sword starts gleaming.")
        print_pause("You unleash your almighty attack on the wizard.")
        print_pause("He is completely vaporized by your strength.")
        print_pause(
            "The whole castle starts to crumble "
            "but you flee the castle in time.")
        print_pause("You saved this land. Excellent job!")
        game_over()
    else:
        print_pause(
            "You try to attack the wizard even though "
            "you have no weapons other than a rusty sword.")
        choices = ['Lucky', 'Not Lucky']
        if random.choice(choices) == "Lucky":
            print_pause(
                "Even so, you manage to plunge your sword "
                "in the wizard's heart.")
            print_pause(
                "Unfortunately, he also managed to hurt you "
                "with a final spell at the same time.")
            print_pause(
                "Both of you die this time but well... "
                "at least you managed to save the land.")
            print_pause("Try for a better ending next time.")
            game_over()
        else:
            print_pause(
                "You didn't manage to get an opening "
                "in the wizard's defenses.")
            print_pause(
                "He promptly vaporizes you while laughing "
                "at your incompetence.")
            game_over()


def walk_stairs(inventory):
    print_pause(
        "Please choose which floor of the castle you want to visit "
        "by entering its respective number:")
    floor = input("1. The lava floor\n"
                  "2. The random sanctuary\n"
                  "3. The cuddly floor\n"
                  "4. Wizard's Den\n")
    if floor == "1":
        first_floor(inventory)
    elif floor == "2":
        second_floor(inventory)
    elif floor == "3":
        third_floor(inventory)
    elif floor == "4":
        fourth_floor(inventory)
    else:
        walk_stairs(inventory)


def start_game():
    inventory = []
    introduction()
    walk_stairs(inventory)


start_game()
