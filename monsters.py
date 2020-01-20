import random
import utilities

# creature class, has name string and size variable
class Mob:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# lists of encounters
# WARNING! Search algorithm means set must contain ONLY other sets OR objects.

beastCommon = [Mob('goblins', 'some'), Mob('giant rats', 'many'), Mob('bandits', 'many')]
beastUncommon = [Mob('mammoth', 'many'), Mob('cockatrice', 'some')]
beastRare = [Mob('griffin', 'one',), Mob('hill giants', 'some')]

monstersAll = [beastCommon, beastUncommon, beastRare]

# Population of monsters, takes a number 1-4 and returns a randomised number
# 1 is singular, 2 is small, 3 is medium, 4 is large
def pop(size):
    if size == 'one':
        return 1
    elif size == 'little':
        return random.randint(1, 4)
    elif size == 'some':
        return random.randint(2, 6)
    elif size == 'many':
        return random.randint(3, 8)
    else:
        print('ERROR!')

# return a mob object based on rarity
def mobRandom():
    chance = random.randint(1, 100);
    if chance in range(1, 60):
        return random.choice(beastCommon)
    elif chance in range(60, 90):
        return random.choice(beastUncommon)
    else: # 80-100
        return random.choice(beastRare)

# return a mob object at random without rarity considered
def mobRandomTrue():
    return utilities.search(monstersAll)
