#!/usr/bin/env python
import random
import roll

def combat():
    x = roll.dtwenty()
    if x > 10:
        return 2
    else:
        return 0
    

