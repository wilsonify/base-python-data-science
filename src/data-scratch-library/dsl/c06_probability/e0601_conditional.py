from enum import Enum
from random import choice


class Kid(Enum):
    # An Enum is a typed set of enumerated values. We can use them
    # to make our code more descriptive and readable.
    BOY = "boy"
    GIRL = "girl"


def random_kid():
    return choice([Kid.BOY, Kid.GIRL])


def simulate():
    both_girls = 0
    older_girl = 0
    either_girl = 0
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == Kid.GIRL:
            older_girl += 1
        if older == Kid.GIRL and younger == Kid.GIRL:
            both_girls += 1
        if older == Kid.GIRL or younger == Kid.GIRL:
            either_girl += 1
    eps = 0.001
    both_girls_given_older = both_girls / (older_girl + eps)
    both_girls_given_older = round(both_girls_given_older, 4)
    both_girls_given_either = both_girls / (either_girl + eps)
    both_girls_given_either = round(both_girls_given_either, 4)
    return both_girls_given_either, both_girls_given_older
