# Imports
import time
import random
import math

game = True
can_hunt = False
jack_can_hunt = True
fire = 100
food = 0
day = 19
day_time = 1
shelter_progress = 0
shelters = 0
ending_type = ""
days_starving = 0
instructions = ""

# Pre-written Mesages
instructions_normal = """
                                Build shelters[BUILD]
                                Gather food[FOOD]
                                Tend to the fire[FIRE]
                                No instructions[SKIP]         
                                """

instructions_hunt = """
                                Build shelters[BUILD]
                                Gather food[FOOD]
                                Tend to the fire[FIRE]
                                No instructions[SKIP]
                                Go hunting[HUNT]         
                                """

link_fire_night_dialoge = f"""
            The sun is setting now and you sit down by the fire. You think about where everything went wrong.
            You look at the fire and the orange flames look quite inviting.

                                {instructions_normal}Link The Fire[LINK]

"""

instructions = instructions_normal


def gather():
    global food
    food += 1
    print("You went and gathered some fruits from the trees and bushes")


def hunt():
    global food
    success = random.randrange(1, 10)
    if success < 6:
        print("The hunt failed and the pig escaped")
    else:
        print("The hunt succeded, time for a feast")
        food += 2


def tend():
    global fire
    print("You tend to the fire")
    fire += 10


def skip():
    print("You don't do anything and time passes by")


def build():
    global shelter_progress
    global shelters
    if shelter_progress == 0:
        print("Started")
    elif shelter_progress == 1:
        print("Kinda done")
    elif shelter_progress == 2:
        print("done")
        shelter_progress = 0
        shelters = 1


def input_handler():
    while True:
        choice = input().upper()
        global game
        global day_time
        global ending_type
        global jack_can_hunt
        if choice == "END":
            quit()
        elif choice == "FOOD":
            gather()
            break
        elif day == 9 and choice == "FIRE":
            jack_can_hunt = False
            game = False
            ending_type = "good"
            break
        elif choice == "FIRE":
            tend()
            break
        elif choice == "SKIP":
            skip()
            break
        elif 9 < day < 15 and choice == "HUNT":
            hunt()
            break
        elif choice == "BUILD":
            build()
            break
        elif day == 16 and choice == "LINK":
            game = False
            ending_type = "good"
            break

        else:
            continue


def morning():
    if day == 1:
        print(f"""
            You wake up after yesterday's meating. All the boys are stadnding around you.
            The moment they see that you have woken up, they ask you:
                What should we do?

                            {instructions}

         """)

    else:
        print(f"We have been here for {day} days")
        print(f"""
            You wake up and ponder to your self. What to do today?
            {instructions}
        """)
    input_handler()


def noon():
    print("noon")
    print(f"""
        The sun is at its apex now it is very hot and everyone is just loitering around. 
        You think that this time could be spent more effectively. 
                    {instructions}
    """)

    input_handler()


def evening():
    global food
    global fire
    global game
    global days_starving
    print("evening")
    # give the player the option to link the fire
    if day == 16:
        print(f"""
            {link_fire_night_dialoge}
        """)
    elif day < 15:
        print(f"""
             The boys have started bathing in the pool. 
            This a nice time for an assembly
            {instructions}
        
        """)
    input_handler()
    if food == 0:
        days_starving += 1
        if days_starving == 3:
            game = False
            ending_type == "bad"
    else:
        days_starving == 0
    food -= 1
    fire -= 20


def normal_day():
    global day_time
    global day
    if day_time == 1:
        morning()
        day_time += 1
    elif day_time == 2:
        noon()
        day_time += 1
    elif day_time == 3:
        evening()
        day_time = 1
        day += 1


def jack_goes_hunting():
    global day
    global jack_can_hunt
    global instructions
    print(""" 
        You notice somthing along the horizon. It looks like a boat.
    """)
    time.sleep(2)
    print("""
            You look over to where the fire is suposed to be, but you see no smoke coming from the foot of the mountain.
    """)
    jack_can_hunt = False
    day += 1
    instructions = instructions_hunt


def day_of_the_splitup():

    print("you go and hunt the beastie because the twins saw it last night")
    time.sleep(2)
    print("you look around the south end of the Island, opposite to the mountain")
    time.sleep(2)
    print("You don't find anything there jsut a cool castlelike rckformation next to the sea")
    time.sleep(2)
    print("You decide to look for the beastie at the mountain where the fire is")
    time.sleep(2)
    print("you arrive at foot of the mountain but the time is getting late.")
    time.sleep(2)
    print("The wind is filled with the ash of the burnt forest from the first night")
    time.sleep(2)
    print("Jack asks you if you want to follow yes/no")

def Second_to_last_day(): 
    print("day 18")
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print("The Savages started throwing rocks at piggy, will you join them? ")
    time.sleep(2)
    choice = input().lower
    if choice == "yes" or choice == "ys":
        global game
        print()
        game = False
        ending_type == "bad"
    elif choice == "no":
        print()

    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    
def Last_day():
    print("day 19")
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print()
    time.sleep(2)
    print("The savages are about to find you, what will you do")
    choice = input().lower
    if choice == "run":
        time.sleep(2)
        print("You started running an quickly ran past the savages")
        time.sleep(2)
        print("They started running after you but quickly lost sight of you")
        time.sleep(2)
        print("The started calling reinforcements")
        time.sleep(2)
        print("The savages are closing in again, what will you do this time?")
        time.sleep(2)
        choice = input().lower
        if choice == "run":
            global game
            print("You once again ran past the savages")
            time.sleep(2)
            print("The savages were faster to react this time and are closing in on you")
            time.sleep(2)
            print("You ran into the bushes and they lost sight of you again")
            time.sleep(2)
            print("There are many hunters around what will you do this time to escape?")
            choice = input().lowr
            if choice == "hide":
                    print("This time you decided that the wiser choice was to hide")
                    time.sleep(2)
                    print("The savages were prepaired for you to run again but were caught off guard when you did not")
                    time.sleep(2)
                    print("They searched every nook and cranny around the area but did not manage to find you")
                    time.sleep(2)
                    print("The savages left the area embarassed and this gave you the chance to get past their defences")
            elif choice == "run":
                print("You started running once again but this time there were to many savages and you did not manage to outrun them")
                ending_type == "bad"
                game = False
            elif choice == "climb":
                print("You fell from the tree while trying to climb")
                ending_type == "bad"
                game = False
            else:
                    print("You took too long thinking")
                    ending_type == "bad"
                    game = False

        elif choice == "climb":
            pass
        elif choice == "hide":
            pass
        else:
            print("You took too long thinking")
            ending_type == "bad"
            game = False
    elif choice == "climb":
        print("You fell from the tree while trying to climb")
        ending_type == "bad"
        game = False
    elif choice == "hide":
        print("You did not hide well enough")
        ending_type == "bad"
        game = False
    # else:
    #     print("You took too long thinking")
    #     ending_type == "bad"
    #     game = False
        
    

def good_ending():
    if day == 9:
        print("Because you tended to the fire, a nearby ship saw the smoke and came to your rescue")
        # boat rescue
    elif day == 17:
        print("""
        In your lowest monent you diced to end it all and rekindle the fire. You stand up and throw yourself into the flames. 
        By offering your soul the age of fire is prolonged and a ship sees the smoke coming from the First Flame. You may have died 
        but you companions survive due to you noble sacrifce.
        """)
        # "Linking the fire"
    else:
        print("You won. yay...")
        # True ending


def bad_ending():
    if day < 18:
        # general bad endings'
        if days_starving == 3:
            print("You were out of food for too long and you starved to death")
        if day == 14:
            print(
                "There was a big storm and because you had no shelters you froze to death")
        if day == 18:
            print("""You joined the savages and started throwing rocks at Piggy, after a while Piggy lost his balance and fell to his death however you weren't bothered by his death. 
                     The day after, rescue came for you but the savages did not want to leave the island and thus you attacked your rescuers. 
                     After that no one tried to save you again and eventually you all starved on the island""")
        if day == 19:
            print("The savages catch up to you and put your head on the double edged stick")


while(game):
    if day == 9:
        morning()
        if jack_can_hunt:
            jack_goes_hunting()
    elif day == 13:
        if shelters < 1:
            game = False
            ending_type = "bad"
        else:
            normal_day()
    elif day == 15:
        instructions = instructions_normal
        pass  # Bestie hunt then Simon gets killed
    elif day == 18:
        Second_to_last_day()
        
    elif day == 19:
        Last_day()
        break
        

    else:
        normal_day()
else:
    if ending_type == "good":
        good_ending()
    elif ending_type == "bad":
        bad_ending()
