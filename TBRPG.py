#!/usr/bin/env python
import time
import random
from TBRPG_Maps import *
from player import *
from enemy import *
import roll
from tables import *

def beginning():
    TBRPG_Maps.slow_clear_screen()
    TBRPG_Maps.welcome()
    TBRPG_Maps.demon()

 
#beginning()

steven = Hero(1, 0)
new_enemy = Enemy(random.randint((steven.lvl), (steven.lvl + 1)), 10)


def combat(new_enemy):
    x = roll.dice(1, 20, 0)
    if x > 10:
        print(new_enemy.lvl)
        new_enemy = Enemy(random.randint((steven.lvl), (steven.lvl + 1)), 10)
        if new_enemy.lvl == 1:
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
        elif new_enemy.lvl == 2:
            new_enemy.xp = 15
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
        elif new_enemy.lvl == 3:
            new_enemy.xp = 20
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
        elif new_enemy.lvl == 4:
            new_enemy.xp = 25
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
        elif new_enemy.lvl == 5:
            new_enemy.xp = 30
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
        elif new_enemy.lvl == 6:
            new_enemy.xp = 40
            print("Enemy level is: " + str(new_enemy.lvl))
            print("You win " + str(new_enemy.xp) + " points!!!")
            steven.xp = steven.xp + new_enemy.xp
            level_up(steven.xp)
            print(stats(steven.lvl, steven.xp))
            roaming()
    else:
        print("You lost the battle... :(")
        roaming()
    
def level_up(exp):
    if exp < exp_table_list[1]:
        steven.lvl = 1
    elif exp >= exp_table_list[1] and exp < exp_table_list[2]:
        steven.lvl = 2
    elif exp >= exp_table_list[2] and exp < exp_table_list[3]:
        steven.lvl = 3
    elif exp >= exp_table_list[3] and exp < exp_table_list[4]:
        steven.lvl = 4
    else:
        steven.lvl = 5


def find_enemy():
    encounter = roll.dice(4, 5, 0)
    if encounter >= 17:
        
        return new_enemy
        # return True
    else:
        return False

def roaming():
        walking = find_enemy()
        if walking == False:
            time.sleep(.5)
            print("Walking....")

            return roaming()
        else:
            time.sleep(.5)
            print("You've encountered an enemy!! Prepare to fight...")

            return combat(new_enemy)
roaming()

answer = raw_input("try again? y/n")
if answer == y:
    roaming()
else:
    print("Bye")

