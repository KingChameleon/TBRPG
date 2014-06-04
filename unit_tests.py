#!/usr/bin/env python
import roll
import player
import combat

# this is for unit tests??
'''
def d_unit_test():
    x = 0
    while x <  100:
        print(roll.three_dfour())
        x += 1
d_unit_test()
'''

# making the hero class
Steven = player.Hero(1, 0)
def gaining_xp():
    win_lose = combat.combat()
    if win_lose == 2:
        Steven.xp = Steven.xp + 2
        congrats = input("You won and gained 2 xp. Your xp is now " + str(Steven.xp) + "")
        if Steven.xp < 10:
            print("You are still level" + str(Steven.lvl) + "!!")
            gaining_levels()
        if Steven.xp >= 10:
            if Steven.xp < 0
            Steven.lvl = Steven.lvl + 1
            print("You are now level " + str(Steven.lvl) + "!!")
    else:
        another_try = input("You lost. Would you llike to fight again?")
        gaining_xp()
   
print(Steven.lvl)

def gaining_levels():
    if Steven.lvl < 3:
        gaining_xp()
    else:
        print("You've reached level 5!!!")


gaining_levels()