'''
Name – Vihaan Shah
Date – 2024-17-22
Description - This is a text based adventure game in Python.
'''

# I imported random so randomized text and integers can be used
import random

# This is just the intro text to the game
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark cave.")
    print("You have a choice to make.\n")

# This is the first choice to enter or leave the cave
def getChoice():
    print("Do you want to:")
    print("1. Enter the cave")
    print("2. Walk away")
    # This is the users input to see if they want to enter or walk away
    choice = input("\nEnter 1 or 2: ")
    # Returns the users choice so that other functions can use it
    return choice

# This is the starting healths for the user and monster
def fightMonster():
    monsterHealth = 10
    playerHealth = 10

    print("\nA monster appears!")

    # This is done so it loops until someone dies
    while monsterHealth > 0 and playerHealth > 0:
        # These display the health
        print(f"Monster health: {monsterHealth}")
        print(f"Your health: {playerHealth}")
        print("Do you want to:")
        print("1. Attack")
        print("2. Run")
        # I can use the variable 'choice' again as it is local to fightMonster()
        choice = input("Enter 1 or 2: ")

        # If the choice was "1", this series of code runs
        if choice == "1":
            # Selects a random int from 1 to 5 and assigns it to the 'attack' variable
            attack = random.randint(1, 5)
            # 'monsterHealth -= attack' is the same as 'monsterHealth = monsterHealth - attack'
            monsterHealth -= attack
            print(f"You attack the monster and deal {attack} damage.")
            # If the monster health is less than 0, you defeated it
            if monsterHealth <= 0:
                print("Congratulations! You defeated the monster!\n")
                # This shows that the user successfully defeated the monster, and ends the fuction
                return True
            monsterAttack = random.randint(1, 5)
            # 'playerHealth -= monsterAttack' is the same as 'playerHealth = playerHealth - monsterAttack'
            playerHealth -= monsterAttack
            print(f"The monster slashes you and deals {monsterAttack} damage!\n")
        elif choice == "2":
            print("You run from the monster you coward!")
            # This shows that the user didn't defeat the monster, and ends the function
            return False
        else:
            # If the user doesn't type 1 or 2 then it automatically runs an attack
            print("Invalid choice. The monster attacks you.")
            monsterAttack = random.randint(1, 5)
            playerHealth -= monsterAttack
            print(f"The monster attacks you and deals {monsterAttack} damage.\n")

        if playerHealth <= 0:
            print("Womp womp womp...you have been defeated by the monster!\n")
            # After the player dies, it ends the code
            return False
    # This ends the function after a player or monster dies
    return False

def caveAdventure():
    print("You enter the cave and find a treasure chest.")
    print("But a monster blocks your path!\n")
    # This starts the fight and assigns the function to the variable
    defeatedMonster = fightMonster()
    # This checks if the player defeated the monster, which would've been True (this is where the return True is also useful)
    if defeatedMonster:
        print("You find a treasure chest!")
        print("Do you want to open it?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            item = random.randint(1, 2)
            # If 'item' is 1, then you found gold
            if item == 1:
                print("Congratulations! You found a pile of gold")
            # And if 'item' is 2, then you found coal
            elif item == 2:
                print("Congratulations! You found a pile of coal")
        elif choice == "2":
            print("You leave the chest alone and exit the cave.")
        else:
            print("Invalid choice! The chest is unopened.")

    # If the user didn't defeat the monster, it prints this as well
    else:
        print("No chest for you!")

# This is the main game funtion which runs the game
def game():
    # Calling the intro function
    intro()
    # Keeps prompting the user for a valid input until one is given
    while True:
        # Puts the function into a variable like we did before
        # This is where the 'return choice' from before comes into play
        choice = getChoice()
        if choice == "1":
            caveAdventure()
            # This ends the loop
            # We didn't use 'return False' this time because we want to continue the game even after the loop ends
            break
        elif choice == "2":
            print("You walk away from the cave. Maybe next time!")
            # Break is also used to end the loop even if it is still true
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# This calls the game() function
game()

