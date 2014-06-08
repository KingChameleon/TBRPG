#!/usr/bin/env python
import roll
import time

def combat():
    x = roll.dice(1, 20, 0)
    if x > 10:
        return True
    else:
        return False
    

def find_enemy():
    encounter = roll.dice(4, 5, 0)
    if encounter >= 17:
        return True
    else:
        return False

def roaming():
    walking = find_enemy()
    if walking == False:
        time.sleep(.5)
        print("Walking....")
        roaming()
    else:
        time.sleep(.5)
        print("You've encountered an enemy!! Prepare to fight...")
        combat()

