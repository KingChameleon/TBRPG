#!/usr/bin/env python
import time
import TBRPG_Maps
from player import *
from enemy import *
from roll import *
from combat import *
from tables import *

def beginning():
    TBRPG_Maps.slow_clear_screen()
    TBRPG_Maps.welcome()
    TBRPG_Maps.demon()

 
#beginning()

steven = Hero(1, 0)

def start_you_roam():
    x = 0
    lose = 0
    win = 0
    while x < 100:
        x += 1
        if roaming():
            win += 1
        else:
            lose += 1
    print("you won " + str(win)  + " times. And lost " + str(lose) + " times.")
start_you_roam()