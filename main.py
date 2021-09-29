game = True
print("""
    You wake up after yesterday's meating and you think to your self:
        What should we do?
            Build shelters[BUILD]
            Gather food[FOOD]
            Tend to fire[FIRE]
            No instructions[SKIP]

                    

""")
while(game):
    choice = input()
    if choice == "end":
        game = False
