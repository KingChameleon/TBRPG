#!/usr/bin/env python
import random

# is a random number generator for your specific dice roll
def dice(number_of_dice, number_of_sides, modifier):
    dice_roll = random.randint(number_of_dice, (number_of_dice * number_of_sides))
    dice_roll = dice_roll + modifier
    return dice_roll

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

