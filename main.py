import random
import monsters
import events
import locations
import utilities


# determine if an encounter exists and find type...
# 0: nothing, 1: creature, 2: event, 3: location, 4: weird
def encounter(chance):
    prob = random.randint(1, 100)
    if prob <= chance: ## something happens!
        encType = random.choice(['mob', 'event', 'location'])
    else: # exit condition...
        return 'nothing happens'
    # stuff happens as prob == 1
    if encType == 'mob': # creature
        mob = monsters.mobRandom()
        return str(monsters.pop(mob.size)) + " " + mob.name
    elif encType == 'event': # event
        return utilities.search(events.events)
    else: # location
        return utilities.search(locations.locations)

# main
running = True
while running:
    print()
    answer = input('input: ')
    print(encounter(40))
    if answer == 'exit':
        running = False
