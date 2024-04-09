#!/bin/python3
import random
import sys
import os

l = [["a", "01"],
     ["i", "02"],
     ["e", "03"],
     ["o", "05"],
     ["z", "06"],
     ["n", "07"],
     ["r", "08"],
     ["w", "09"],
     ["s", "0A"],
     ["c", "0B"],
     ["t", "0C"],
     ["y", "0D"],
     ["k", "0E"],
     ["d", "0F"],
     ["h", "20"],
     ["l", "21"],
     ["u", "22"],
     ["m", "23"],
     ["f", "24"],
     ["g", "25"],
     ["p", "26"],
     ["b", "27"],
     ["v", "28"],
     ["j", "29"],
     ["x", "2A"],
     ["q", "2B"]]

def getch():
    import sys, termios, tty

    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)



while True:
    r = random.choice(l)
    mistakeCount = 0
    
    while True:
        os.system('clear')
        print(r[0])
        if mistakeCount > 2:
            print(r[1])
        print()
        i = getch()
        if i == r[0]:
            break
        if i == "$":
            exit()
        if i != r[0]:
            mistakeCount += 1
    
