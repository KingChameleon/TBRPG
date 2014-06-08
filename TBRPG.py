#!/usr/bin/env python
import time
import TBRPG_Maps
from player import *
from enemy import *
from roll import *
from combat import combat
from tables import *

def beginning():
    TBRPG_Maps.slow_clear_screen()
    TBRPG_Maps.welcome()
    TBRPG_Maps.demon()

 
#beginning()

steven = Hero(1, 0, 2, 5)


'''
if steven.lvl == 1:
    replace_value(player_intelligence_dict, 'spell_power_modifier', 5)
'''
print(player_intelligence_dict['spell_power_modifier'])
print(find_value(player_intelligence_dict, 'spell_power_modifier'))