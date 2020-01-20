import random

# searching algorithm, randomly searches through sets until it chooses something at the lowest level
# RETURNS object
# recursive
def search(target):
    if isinstance(target, list) == False:
        return target
    return search(random.choice(target))
