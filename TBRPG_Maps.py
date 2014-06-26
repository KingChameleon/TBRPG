#!/usr/bin/env python
import time

def clear_screen():
    for i in range(18):
        print("\n")

def slow_clear_screen():
    for i in range(12):
        print("\n")
        time.sleep(.25)

def slow_welcome():
    print("\n \n")
    time.sleep(.137)
    print(r" __     __   ______   __       ______   ______   __    __   ______ ")
    time.sleep(.137)
    print(r"/\ \  _ \ \ /\  ___\ /\ \     /\  ___\ /\  __ \ /\ '-./  \ /\  ___\  ")
    time.sleep(.137)
    print(r"\ \ \/ '.\ \\ \  __\ \ \ \____\ \ \____\ \ \/\ \\ \ \-./\ \\ \  __\ ")
    time.sleep(.137)
    print(r" \ \__/'.~\_\\ \_____\\ \_____\\ \_____\\ \_____\\ \_\ \ \_\\ \_____\ ")
    time.sleep(.137)
    print(r"  \/_/   \/_/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/  \/_/ \/_____/")
    for i in range(8):
        print("\n")
        time.sleep(.137)
        
def welcome():
    with open("welcome.txt") as f:
        for i in f:
            str1 = i.replace('\n', '')
            print(str1)
            time.sleep(.25)
            # print(f.read())
        time.sleep(2)
        slow_clear_screen()

def demon():
    with open("demon.txt") as f:
        print(f.read())
        
def stats(lvl, exp):
    print(r"+----------------------------------------------------+")
    print(r"  Hero    |   Level   |  Experience  |   Damage  ")
    print(r"+----------------------------------------------------+")
    if len(str(lvl)) == 2:
        print(r"  Steven  |     " + str(lvl) + "     |      " + str(exp) + "      |      2    ")
    else:
        print(r"  Steven  |      " + str(lvl) + "    |      " + str(exp) + "      |      2    ")
    '''
    if len(str(creature)) == 2:
        print(r"  Demon   |     " + str(creature) + "      |      0       |      2       ")
    else:
        print(r"  Demon   |      " + str(creature) + "      |      0       |      2       ")
    print(r"+----------------------------------------------------+")
    '''
        
def steven():
    with open("steven.txt") as f:
        print(f.read())




def level_one():
    board = []
    x = 0
    while x < 10:
        board.append(["x"] * 10)
        x += 1
    return board

def print_board(x):
    for i in x:
        print(" ".join(i))