import random
from library import name_prefix, name_suffix, name_tag

# ---------- RANDOM STAR/PLANET NAME ---------- #
def random_name (pre=random.randint(1,1000), suf=random.randint(1,1000), tag=random.randint(1,98), pre_only=random.randint(1,100), star=False, planet=False, include_tag=False):
    pre_text = name_prefix[pre]
    suf_text = name_suffix[suf]

    if include_tag:
        tag_text = " " + name_tag[tag]
    else:
        tag_text = ''

    if pre_only > 95:
        suf_text = ''

    return (f'{pre_text}{suf_text}{tag_text}')

print(random_name(include_tag=True))

