#!/usr/bin/env python
import random

# returns a random number between 1 and 20
def dtwenty():
    d_20 = random.randint(1, 20)
    return d_20

# returns a random number between 1 and 100
def dpercent():
    d_tens_place = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    d_tens_place = random.choice(d_tens_place)
    d_ones_place = random.randint(0, 9)
    if d_tens_place == 00:
        if d_ones_place == 0:
            return 100
        else:
            return d_ones_place
    else:
        return (d_tens_place + d_ones_place)

# returns a random number between 4 and 15
def three_dfour():
    one_dfour = random.randint(0, 4)
    two_dfour = random.randint(0, 4)
    three_dfour = random.randint(0, 4)
    total_dfour = (one_dfour + two_dfour + three_dfour + 3)
    return total_dfour
    