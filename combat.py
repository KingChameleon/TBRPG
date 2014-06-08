#!/usr/bin/env python
import roll

def combat():
    x = roll.dice(1, 20, 0)
    if x > 10:
        return True
    else:
        return False
    

