import random


# Generates an array of random grid coordinates to create a system.
def create_system_set(row=10, col=8):
    system_set = set()
    num_systems = ((row * col * 0.25) + random.randint(1, 10))
    threshold = num_systems / (row * col)
    for r in range(row):
        for c in range(col):
            test = random.random()
            if test < threshold:
                system_set.add((r, c))

    return system_set
