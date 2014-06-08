#!/usr/bin/env python
import time
import TBRPG_Maps
from player import *
from enemy import *
from roll import *
from combat import *
from tables import *

def beginning():
    #TBRPG_Maps.slow_clear_screen()
    #TBRPG_Maps.welcome()
    TBRPG_Maps.demon()

 
#beginning()

steven = Hero(1, 0)

def start_you_roam():
    looking_for_a_fight = roaming()
    if looking_for_a_fight == True:
        outcome = combat()
        if outcome == False:
            print("You lost.")
        else:
            print("You won!")
start_you_roam()