import random
from library import name_prefix, name_suffix, name_tag


# ---------- RANDOM STAR/PLANET NAME ---------- #
def random_name(pre=random.randint(1, 1000), suf=random.randint(1, 1000), tag=random.randint(1, 98),
                pre_only=random.randint(1, 100), star=False, planet=False, include_tag=False):
    pre_text = name_prefix[pre]
    suf_text = name_suffix[suf]

    if include_tag:
        tag_text = " " + name_tag[tag]
    else:
        tag_text = ''

    if pre_only > 90:
        suf_text = ''

    return f'{pre_text}{suf_text}{tag_text}'


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