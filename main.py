# Imports
import time
import random


# Variables
game = True
can_hunt = False
jack_can_hunt = True
fire = 100
food = 0
day = 1
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

# Functions for Player Actions


def gather():
    global food
    food += 1
    input("You went and gathered some fruits from the trees and the bushes")


def hunt():
    global food
    success = random.randrange(1, 10)
    if success < 6:
        input("The hunt failed and the pig escaped")
    else:
        input("The hunt succeeded, time for a feast")
        food += 2


def tend():
    global fire
    input("You tend to the fire")
    fire += 10


def skip():
    input("You don't do anything and time passes by")


def build():
    global shelter_progress
    global shelters
    if shelter_progress == 0:
        input("You and some other boys start bulding a shelter")
        shelter_progress += 1
    elif shelter_progress == 1:
        input("You continue building the shelter.")
        shelter_progress += 1
    elif shelter_progress == 2:
        input("You add the final touches to the shelter.")
        input("It's finally done.")
        shelter_progress = 0
        shelters += 1


def stat_check():
    print(f"\nFood: {food}")
    print(f"Fire: {fire}")
    print(f"Shelters: {shelters}")
    print(f"Shelter build progress: {shelter_progress}\n")

# Devfeature


def change_day():
    global day, day_time
    day = int(input("Which day do you want to skip to?"))
    day_time = 1

# Input handler


def input_handler():
    while True:
        choice = input("\n").upper()
        global game, day_time, ending_type, jack_can_hunt
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
    if day < 15:
        print(f"""
            The sun is at its apex now it is very hot and everyone is just loitering around. 
            You think that this time could be spent more effectively. 
                        {instructions}
        """)
    elif day >= 15:
        print(f"""
            The sun is at its apex now and it is scorching hot.
            But this can't hinder you. There should be somthing to be done.
                        {instructions}
        
        """)
    input_handler()


def evening():
    global food, fire, game, days_starving, ending_type
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
        print(f"""
            The sun is setting but there should still be time for one more thing.
            {instructions}
        """)
    input_handler()
    if food == 0:
        days_starving += 1
        if days_starving == 3:
            game = False
            ending_type = "bad"
    else:
        days_starving == 0
        food -= 1
    if fire >= 20:
        fire -= 20
    else:
        fire -= 10


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

# Scripted Events


def jack_goes_hunting():
    global day, jack_can_hunt, instructions, day_time
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
    input("The boys quiet down.")
    input("Everyone feels down so you wait with giving them orders until tomorrow.")
    jack_can_hunt = False
    day += 1
    day_time = 1
    instructions = instructions_hunt


def day_of_the_splitup():
    global instructions, day, day_time
    input("you go and hunt the beastie because the twins saw it last night")
    input("you look around the south end of the Island, opposite to the mountain")
    input("You don't find anything there just a cool castlelike rockmation next to the sea")
    input("You decide to look for the beastie at the mountain where the fire is")
    input("you arrive at foot of the mountain but the time is getting late.")
    input("The wind is filled with the ash of the burnt forest from the first night")
    print("Jack asks you if you want to follow yes/no")
    choice = input().lower()
    if choice == "yes" or choice == "ys":
        input("You follow Jack up the mountain. The ash in the wind hurts your eyes but you push through.")
        input("When you get on the top of the mountain you sea a man twisted in his parachute.")
        input("Knowing what the beast was you start climbing of the mountain.")
        input("When you get to the foot of the mountain and meet up with the rest of the group Jack suddenly yells.")
        input("I had enough of Ralph's incompetent leadership.")
        input("I am starting my own tribe. Who want's to join?")
        input("Almost all of the boys put up their hands.")
        input("This caches you by surprise and you don't know what to say.")
        input("We will have a feast tonight to celebrate the creation of my new tribe")
        input("And for those who had not made up their minds yet.")
        input("You guys can still come to the feast. Everyone is welcome!")
        input("And before you realise all of the boys have gone of with Jack")

    elif choice == "no":
        input("You decide to stay")
        input("Jack comes back. He says he killed the beast and accuses you of being unfit to be their leader.")
        input("He tells the other boy that if they want a better leader, they should follow him.")
        input("Then he says that he's going to have a feast and everyone is welcome there")
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
        input("You catch a glimpse of the face of the beast.")
        input("It looks like Simon.")
        input("Suddenly the beast cries out in pain and runs toward the ocean.")
        input("After that nither the beast nor Simon is ever seen again.")
    elif choice == "no":
        input("You decide not to go to the feast")
        input("It is getting late so you decide to go to sleep")
        input("On your way to the shelters Piggy comes to you and tells you that Simon has been missing all day and he hasn't come back yet")
        input("You tell Piggy not to worry and go to sleep")
        time.sleep(5)
        input("But Simon never came back\n")
    day += 1
    day_time = 1
    instructions = instructions_normal


def Second_to_last_day():
    global day, ending_type
    input("Last night the savages came by and took Piggy's glasses")
    input("Piggy, the twins and you decide to go to where the savages are and try to talk some sense into them.")
    input("Piggy picks up the conch and everyone starts walking toward the hideout of the savages")
    input("Jack comes out with the rest of the tribe behind him")
    input("Piggy goes forward and starts talking to them, but they don't seem to be listening")
    input("Suddenly a savage throws a stone at Piggy. Soon after the rest of the tribe joins in.")
    print("Will you join them? ")
    choice = input().lower()
    if choice == "yes" or choice == "ys":
        global game
        game = False
        ending_type = "bad"
    elif choice == "no":
        input("You decide not to join in.")
        input("After a while the stoning stops and you think this was it.")
        input("But out of nowhere a giant boulder comes rolling towards Piggy.")
        input("Piggy gets hit by the rock and falls into the ocean.")
        input("Don't know what to do.")
        input("So you just run away, leaving the twins in the hands of the savages")
        time.sleep(3)
        print()
        time.sleep(3)
        print()
        time.sleep(3)
        print()
        time.sleep(1)
        input("It's getting late now.")
        input("You wonder what's happened to the twins.")
        input("You go back to the Savage Hideout")
        input("When you get close you see that two people are guarding the entrance")
        input("It must be the twins")
        input("You walk up to them and ask how they have been doing.")
        input("They inform you that they have been treated well")
        input("But they have som bad news for you.")
        input('Jack is planing to hunt you and use a "double edged stick"')
        input("You tell them not to worry and sya good bye")
        input("You decide that hiding in the tall grass near the hiedout is the best idea")
        input("You walk there lie down and go to sleep\n")
        day += 1


def Last_day():
    global game
    global last_choice
    global ending_type
    input("You wake up in the tall grass to the sound of the ululation of the savages.")
    input("You run away and hide.")
    print("But after a while you can hear the savages closing in. What will you do?")
    while last_choice < 3:
        choice = input("run[RUN] climb[CLIMB] or hide[HIDE]\n").upper()
        if choice == "RUN":

            if last_choice == 0:
                input("You started running an quickly ran past the savages")
                input("They started running after you but quickly lost sight of you")
                input("They have called in reinforcements")
                print("The savages are closing in again, what will you do this time?")
            elif last_choice == 1:
                input("You once again ran past the savages")
                input(
                    "The savages were faster to react this time and are closing in on you once more")
                input("You ran into the bushes and they lose sight of you again")
                print(
                    "There are many hunters around what will you do this time to escape?")
            elif last_choice == 2:
                print(
                    "You started running once again but this time there were to many savages and you did not manage to outrun them")
                ending_type = "bad"
                game = False
                break
            last_choice += 1
        elif choice == "CLIMB":
            print("You fell from the tree while trying to climb")
            ending_type = "bad"
            game = False
            break
        elif choice == "HIDE":
            if last_choice == 2:
                input("This time you decided that the wiser choice was to hide")
                input(
                    "The savages were prepaired for you to run again but were caught off guard when you did not")
                input(
                    "They searched every nook and cranny around the area but did not manage to find you")
                input(
                    "The savages left the area embarrassed and this gave you the chance to get past their defences")
                ending_type = "good"
                game = False
                break
            else:
                print("You did not hide well enough and the savages find you")
                ending_type = "bad"
                game = False
                break

        else:
            print("You took too long thinking")

            ending_type = "bad"
            game = False

# Endings


def good_ending():
    if day == 9:
        print("Because you tended to the fire, a nearby ship saw the smoke and came to your rescue")
        # boat rescue
    elif day == 17:
        print("""
        In your lowest moment you decide to end it all and rekindle the fire. You stand up and throw yourself into the flames. 
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
        elif day == 13:
            print(
                "There was a big storm and because you had no shelters you froze to death")
        elif day == 18:
            print("""You joined the savages and started throwing rocks at Piggy, after a while he lost his balance and fell to his death however you weren't bothered by that. 
                     The day after, rescue came for you but the savages did not want to leave the island and thus you attacked your rescuers. 
                     After that no one tried to save you again and eventually you all starved on the island""")
        elif day == 19:
            print(
                "The savages catch up to you and put your head on the double edged stick")
        else:
            print("You lost \N{Skull}")


if day == 1:
    input("""

        Yesterday you and some other boys got stranded on an island. First you met a fat boy named Piggy. The two of you found a conch.
        You blew into the conch, which made a loud noise that could be heard all over the island. After a short while, boys started 
        coming your way, because they heard the sound of the conch. When no more boys were coming, you and the others decided to hold 
        an assembly. On this assembly the group decied that you will be their chief. A boy called Jack volunteered himself and the 
        choir he was leading to be hunters. This concluded the assembly. The sun was setting. You decided to go to sleep after this long day.


                                                        Press ENTER to continue

    """)
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
