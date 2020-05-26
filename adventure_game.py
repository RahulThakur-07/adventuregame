import time
import random


enemy_list = ["Pirate", "Troll", "Dragon", "School Principal", "Alien", "Beast", "Wicked fairie"]
enemy = random.choice(enemy_list)
weapon_list = ["nothing", "wooden sword", "knife", "metal sword", "gun"]
player_weapon = "nothing"
health = {
        "Wicked fairie" : 40,
        "Pirate" : 50,
        "Troll" : 70,
        "Dragon" : 80,
        "School Principal" : 90,
        "Alien": 100
    }
random_situation = [1,2]

def print_pause(message):
    print(message)
    time.sleep(2)

def field():
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house. \n")
    print_pause("Enter 2 to peer into the cave. \n")
    print_pause("What would you like to do?  \n")
    while True:
            choice1 = input("Please enter 1 or 2.\n")
            if choice1 == "1":
                house()
                break
            elif choice1 == "2":
                cave()
                break 
                    
def house():
    # Things that happen to the player in the house
    print_pause("Going towards house and now knocking the door.\n")
    random_number = random.choice([1,2])
    if(random_number == 1):
        danger() 
    else:
        safe()

def cave():
    # Things that happen to the player goes in the cave  
    print_pause("Going towards cave and now peeping in the cave.\n")
    random_number = random.choice([1,2])
    if(random_number == 2):
        danger() 
    else:
        safe()


def danger():
    print_pause("Oops wrong decision, "+enemy+" is here!")
    print_pause("Enter 1 to to fight with "+enemy+" \n")
    print_pause("Enter 2 to run back to field. \n")
    print_pause("What would you like to do?  \n")
    while True:
            choice = input("Press 1 or 2\n")
            if choice == "1":
                    print_pause("Fighting\n")      
                    global player_weapon   
                    fight(player_weapon)
                    break
            elif choice == "2":
                    print_pause("Running back to field...\n")
                    field()
                    break 

def safe():
    print_pause("It seems no one is here.")
    print_pause("Enter 1 to search for something. \n")
    print_pause("Enter 2 to go back to field. \n")
    print_pause("What would you like to do?  \n")
    while True:
            choice = input("Press 1 or 2\n")
            if choice == "1":
                    print_pause("Searching..")      
                    global player_weapon                 
                    player_weapon = random.choice(weapon_list)
                    print_pause("Yeah! you got "+player_weapon+" and its damage is "+ str(weapon_damage(player_weapon))+" \n") 
                    print_pause("Now, going to field...\n")
                    field()
                    break
            elif choice == "2":
                    print_pause("Going to field...\n")
                    field()
                    break 
def weapon_damage(weapon):
    if(weapon == "nothing"):
        return 20
    elif weapon == "wooden sword":
        return 45
    elif(weapon == "knife"):
        return 55
    elif(weapon == "metal sword"):
        return 75
    elif(weapon == "gun"):
        return 95


def fight(weapon):
    # Things that happen when the player fights  
    global enemy
    enemy_health = health.get(enemy)
    if(weapon_damage(weapon) > enemy_health):
        print_pause("You won!!\n\n")
    else:
        print_pause("You were killed\n\n")



def play_game():
    global enemy 
    while True:
            print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")
            print_pause("Rumor has it that a "+ enemy +" is somewhere around here, and has been terrifying the nearby village.\n")
            print_pause("In front of you is a house.\n")
            print_pause("To your right is a dark cave.\n")
            print_pause("In your hand you hold your trusty but not very effective dagger.\n")

            field()

            play_again()
            break

def play_again():
    print_pause("GAME OVER\n\n")
    while True:
            playagain = input("Would you like to play again? (y/n)\n")
            if playagain == "y":
                    print_pause("Starting game again\n")                       
                    enemy = random.choice(enemy_list)
                    play_game()  
                    break
            elif playagain == "n":
                    print_pause("Exiting game...\n\n")
                    break 

play_game()
    