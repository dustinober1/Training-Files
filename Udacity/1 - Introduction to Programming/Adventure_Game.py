import time
import random

# make a blank item bracket to append to later
item = []

# make random choices
enemies = ["pirate", "dragon", "troll"]
option = random.choice(enemies)


# play agan when needed
def play_again():
    again = input("Try Again? (y/n)\n\n")
    if again == "y":
        print_pause("\n\nRestarting the game....\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\nSee you next time\n\n")
        exit()
    else:
        print("I dont understand")
        play_again()


# for messages to play slower
def print_pause(message_printed, pause=0.5):
    print(message_printed)
    time.sleep(pause)


# intro scenario
def intro():
    print_pause("You are going to mama rose's house")
    print_pause("There are rumors of pirates, dragons, and trolls")
    print_pause("You get turned around and see two paths")
    print_pause("The left path is a torn up path")
    print_pause("The right path is a smooth road")
    print_pause("Your heartrate increases and you are getting nervious")


# scenario to choose what to do at the door
def rough_path():
    option = random.choice(["pirate", "dragon", "troll"])
    print_pause("You approach the rough path")
    print_pause(f"You are about 1/4 miles when "
                "you see a " + option + ".")
    print_pause(f"The rumored " + option + " is not a rumor!")
    print_pause(f"The " + option + "'s are real!")
    print_pause(f"The " + option + " comed towards you\n")
    if "horse" not in item:
        print_pause("You are not sure if you can run past them")
        print_pause("You are not a fast runner")
    while True:
        runto_runaway = input("Would you like to"
                              "(1) run aroud or"
                              "(2) run away\n")
        if runto_runaway == "1":
            if "horse" in item:
                print_pause("\nAs the " + option + " moves to attach, "
                            "you unleash hell on your new horse.")
                print_pause("The horse runs and runs and gets"
                            "around the " + option + ".")
                print_pause("The " + option + " takes one swipe at"
                            "you. It was close, but the " + option + " missed")
                print_pause("You have gotten around the " + option +
                            " and continued your journey")
            else:
                print_pause("Your try your best to get"
                            "around the " + option + ".")
                print_pause("You are too slow, the " + option +
                            "attacks you")
                print_pause("You lose")
            play_again()
            break
        if runto_runaway == "2":
            print_pause("You run back to the intersection"
                        " luckly you dont seem to be followed")
            left_right()


# What happends if the player chooses the cave
def smooth_path():
    if "horse" in item:
        print_pause("You walk down the smooth road")
        print_pause("This is where you found your horse")
        print_pause("There is nothing here but a dead end")
        print_pause("You ride back to the intersection\n")
        left_right()
    else:
        print_pause("You walk down the smooth road")
        print_pause("You find a horse tied to a tree")
        print_pause("The horse has your name written on it")
        print_pause("You jump on the hourse and head back")
        item.append("horse")
        left_right()


# player making the choice between the door or the cave
def left_right():
    print_pause("Enter 1 to take the rough path")
    print_pause("Enter 2 to take the smooth path")
    choice1 = input("Please enter 1 or 2.\n")
    if choice1 == "1":
        rough_path()
    elif choice1 == "2":
        smooth_path()
    else:
        print("I dont understand")
        left_right()


# playing the game.
def play_game():
    intro()
    left_right()


play_game()
