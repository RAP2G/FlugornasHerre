# Imports
import time


game = True
fire = 100
fruit = 1000
food = 0
pigs = 10
day = 1
day_time = 1
boys = 18
shelter_progress = 0
shelters = 0


def gather():
    global food
    print(food)


def hunt():
    pass


def tend():
    global fire
    print("You tend to the fire")
    fire += 5


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


def morning():
    if day == 1:
        print("""
            You wake up after yesterday's meating. All the boys are stadnding around you.
            The moment the ysee that you have woken up, they ask you:
                What should we do?

                    Build shelters[BUILD]
                    Gather food[FOOD]
                    Check the fire[FIRE]
                    No instructions[SKIP]                 

         """)
    elif day == 9:
        pass
    else:
        print(f"We have been here for {day} days")
        print("""
            You wake up and ponder to your self. What to do today?
        """)

    choice = input()
    global game
    if choice == "end":
        game = False
    elif choice == "FOOD":
        gather()


def noon():
    print("noon")
    print("""
        The sun is at its apex now it is very hot and everyone is just loitering around. 
        You think that this time could be spent more effectively. 
    """)
    choice = input("What should the other boys do?")
    if choice == "end":
        global game
        game = False
    elif choice == "FOOD":
        gather()


def evening():
    print("evening")
    print("""
        The sun is setting now. The boys have started bathing in the pool. 
        This  a nice time for a
    
    """)
    choice = input()
    if choice == "end":
        global game
        game = False
    elif choice == "FOOD":
        gather()


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
    morning()
    print(""" 
        You notice somthing along the horizon. It looks like a boat.
    """)
    time.sleep(2)
    print("""
            You look over to where the fire is suposed to be, but you see no smoke coming from the foor of the mountin.
    """)


while(game):
    if day == 9:
        jack_goes_hunting()
    else:
        normal_day()
