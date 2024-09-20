from typing import List
from random import choice

FUZZY_SEARCH_THRESHOLD = 20


def pick_random_object(objects: List[int]):
    return choice(objects[0:FUZZY_SEARCH_THRESHOLD])
