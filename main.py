# Imports
import time
import random
import math


# Variables
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
last_choice = 0

# Pre-written Mesages
instructions_normal = """
                                Build shelters[BUILD]
                                Gather food[FOOD]
                                Tend to the fire[FIRE]
                                No instructions[SKIP]     
                                Stats[STATS]    
                                """

instructions_hunt = """
                                Build shelters[BUILD]
                                Gather food[FOOD]
                                Tend to the fire[FIRE]
                                No instructions[SKIP]
                                Go hunting[HUNT]        
                                Stats[STATS]    
                                """

link_fire_night_dialogue = f"""
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
        print("The hunt succeeded, time for a feast")
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


def stat_check():
    print("")
    print(f"Food: {food}")
    print(f"Fire: {fire}")
    print(f"Shelters: {shelters}")
    print(f"Shelter build progress: {shelter_progress}")


def change_day():
    global day
    global day_time
    day = int(input("Which day do you want to skip to?"))
    day_time = 1


def input_handler():
    while True:
        choice = input("\n").upper()
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
        elif 9 < day and day < 15 and choice == "HUNT":
            hunt()
            break
        elif choice == "BUILD":
            build()
            break
        elif day == 16 and day_time == 3 and choice == "LINK":
            game = False
            ending_type = "good"
            break
        elif choice == "DAYS":
            change_day()
            break
        elif choice == "STATS":
            stat_check()
        else:
            continue


def morning():
    if day == 1:
        print(f"""
            You wake up after yesterday's meating. All the boys are standing around you.
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
    if day == 16:
        print(f"""
            {link_fire_night_dialogue}
        """)
    elif day < 15:
        print(f"""
            The boys have started bathing in the pool after a long day.
            There should be time for one more thing before it gets too dark.
            {instructions}
        
        """)
    elif day >= 15:
        pass
    input_handler()
    if food == 0:
        days_starving += 1
        if days_starving == 3:
            game = False
            ending_type == "bad"
    else:
        days_starving == 0
    food -= 1
    if fire > 20:
        fire -= 20
    else:
        fire = fire-fire


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
    input(""" 
        You notice somthing along the horizon. It looks like a boat.\n
    """)

    input("""
        You look over to where the fire is supposed to be, but you see no smoke coming from the foot of the mountain.\n
    """)

    input("""
        You decide to run over to the fire.\n
    """)
    input("""
        When you arrive the fire is out. The twins are nowhere to be seen.\n
    """)
    input("After a short while you spot Jack, a couple of the other boys and the twins coming back with a dead pig on their shoulders.\n")
    input('''
        When they spot you they speed up and while they are getting closer you hear them  chant:
                        "Kill the pig. Cut her throat. Spill her blood."

    ''')
    input(''' 
        When the boys arrive they start boasting about their hunt.
                "Look! We've killed a pig -we stole up on them- we got in a circle-"
                "We got in a circle-"
                "We crept up-"
                "The pig squealed-" 
    ''')
    input("When they calm down a bit you say: You let the fire go out.")
    input("You also tell them that a ship passed by.")
    input("Everyone feels down so you wait with giving them orders until tomorrow.")
    jack_can_hunt = False
    day += 1
    instructions = instructions_hunt


def day_of_the_splitup():

    input("you go and hunt the beastie because the twins saw it last night")
    input("you look around the south end of the Island, opposite to the mountain")
    input("You don't find anything there just a cool castlelike rockmation next to the sea")
    input("You decide to look for the beastie at the mountain where the fire is")
    input("you arrive at foot of the mountain but the time is getting late.")
    input("The wind is filled with the ash of the burnt forest from the first night")
    print("Jack asks you if you want to follow yes/no")
    choice = input().lower()
    if choice == "yes" or choice == "ys":
        input("You follow jack up the mountain. The ash in the wind hurts your eyes but you push through.")
        input("When you get on the top of the mountain ")
    elif choice == "no":
        input("You decide to stay")
        input("Jack comes back. He says he killed the beast and accuses you of being unfit to be their leader.")
        input("He tells the other boy that if they want a better leader, they should follow him.")
        input("Then he says that he's going to have a feast and everyone id welcome there")
        input("You get back to Piggy and the twins and tell them what has happened")
        input("They can't believe what you've told them")
    input("It is getting late you and you companions are getting hungry")
    print("Do you want to go to the feast yes/no")
    choice = input().lower()
    if choice == "yes" or choice == "ys":
        input("You decide to go to the feast")
        input("When you get there, you see the rest of the boys and the Littleuns sitting around the fire, etaing.")
        input("Jack throws you a peace of meat.")
        input("You pick it up and start eating it.")
        input(
            'After a while Jack suddenly stands up and says "Do our dance! Come on! Dance!"')
        input('All the boys stand upp and start dancing in a ring while chanting "Kill the pig. Cut her throat. Spill her blood."')
        input("You join in.")
        input("After a while a black hairy beast comes out of the forest and enters the ring of dancing boys.")
        input("The boys start stabbing at the beast with their spears.")
    elif choice == "no":
        input("You decide not to go to the feast")
        input("It is getting late so you decide to go to sleep")
        input("On your way to the shelters Piggy comes to you and tells you that Simon has been missing all day and he hasn't come back yet")
        input("You tell Piggy not to worry and go to sleep")
        time.sleep(5)
        input("But Simon never came back")


def Second_to_last_day():
    print("day 18")
    print("The Savages started throwing rocks at piggy, will you join them? ")
    choice = input().lower()
    if choice == "yes" or choice == "ys":
        global game
        print()
        game = False
        ending_type == "bad"
    elif choice == "no":
        print()


def Last_day():
    global game
    global last_choice
    global ending_type
    print("day 19")
    print("The savages are about to find you, what will you do")
    while last_choice < 3:
        choice = input().upper()
        print(choice)
        if choice == "RUN":

            if last_choice == 0:
                print("You started running an quickly ran past the savages")
                print("They started running after you but quickly lost sight of you")
                print("The started calling reinforcements")
                print("The savages are closing in again, what will you do this time?")
            elif last_choice == 1:
                print("You once again ran past the savages")
                print(
                    "The savages were faster to react this time and are closing in on you")
                print("You ran into the bushes and they lost sight of you again")
                print(
                    "There are many hunters around what will you do this time to escape?")
            elif last_choice == 2:
                print(
                    "You started running once again but this time there were to many savages and you did not manage to outrun them")
                ending_type == "bad"
                game = False
                break
            last_choice += 1
        elif choice == "CLIMB":
            print("You fell from the tree while trying to climb")
            ending_type == "bad"
            game = False
            break
        elif choice == "HIDE":
            if last_choice == 2:
                print("This time you decided that the wiser choice was to hide")
                print(
                    "The savages were prepaired for you to run again but were caught off guard when you did not")
                print(
                    "They searched every nook and cranny around the area but did not manage to find you")
                print(
                    "The savages left the area embarrassed and this gave you the chance to get past their defences")
                ending_type = "good"
                game = False
                break
            else:
                print("You did not hide well enough and the savages find you")
                ending_type == "bad"
                game = False
                break
            last_choice += 1

        else:
            print("You took too long thinking")

            ending_type == "bad"
            game = False


def good_ending():
    if day == 9:
        print("Because you tended to the fire, a nearby ship saw the smoke and came to your rescue")
        # boat rescue
    elif day == 17:
        print("""
        In your lowest moment you diced to end it all and rekindle the fire. You stand up and throw yourself into the flames. 
        By offering your soul the age of fire is prolonged and a ship sees the smoke coming from the First Flame. You may have died 
        but you companions survive due to you noble sacrifice.
        """)
        # "Linking the fire"
    elif day == 19:
        input("You run to the beach with the sound of the savages behind you.")
        input("On the beach you tumble and fall.")
        input("You think that you are going to die but when you look up you see the face of an old man.")
        print("He smiles and says to you: How's it going boyo? Rescue is here.")
    else:
        print("You won. yay...")


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
            print(
                "The savages catch up to you and put your head on the double edged stick")


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
        day_of_the_splitup()
    elif day == 18:
        morning()
        Second_to_last_day()

    elif day == 19:
        Last_day()
    else:
        normal_day()
else:
    if ending_type == "good":
        good_ending()
    elif ending_type == "bad":
        bad_ending()
