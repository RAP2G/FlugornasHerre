global game
game = True
fire = 100
fruit = 1000
food = 0
pigs = 10
day = 1
day_time = 1


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
    else:
        print(f"We have been here for {day} days")

    choice = input()
    if choice == "end":
        global game
        game = False
    elif choice == "FOOD":
        gather()


def noon():
    print("noon")
    choice = input()
    if choice == "end":
        global game
        game = False
    elif choice == "FOOD":
        gather()


def evening():
    print("evening")
    choice = input()
    if choice == "end":
        global game
        game = False
    elif choice == "FOOD":
        gather()


def gather():
    print(food)
    day_time


while(game):
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
