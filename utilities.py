import random


# Generates an array of random grid coordinates to create a system.
def create_system_set(num_systems=(20+random.randint(1,10)), row=10, col=8):
    system_set = set()
    threshold = num_systems / (row * col)
    for r in range(row):
        for c in range(col):
            test = random.random()
            if test < threshold:
                system_set.add((r, c))

    return system_set
