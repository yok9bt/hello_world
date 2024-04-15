#!/bin/python3
import random
import os
import time

def getch():
    import sys, termios, tty
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

l = [["a", "01", 0],
     ["i", "02", 0],
     ["e", "03", 0],
     ["o", "05", 0],
     ["z", "06", 0],
     ["n", "07", 0],
     ["r", "08", 0],
     ["w", "09", 0],
     ["s", "0A", 0],
     ["c", "0B", 0],
     ["t", "0C", 0],
     ["y", "0D", 0],
     ["k", "0E", 0],
     ["d", "0F", 0],
     ["h", "20", 0],
     ["l", "21", 0],
     ["u", "22", 0],
     ["m", "23", 0],
     ["f", "24", 0],
     ["g", "25", 0],
     ["p", "26", 0],
     ["b", "27", 0],
     ["v", "28", 0],
     ["j", "29", 0],
     ["x", "2A", 0],
     ["q", "2B", 0]]

startGameTime = time.time()
lr = [0]
while True:
    while True:
        r = random.choice(l)
        if r[0] != lr[0]:
            lr = r
            break
    mistakeCount = 0
    while True:
        os.system('clear')
        print(r[0])
        if mistakeCount > 2:
            print(r[1])
        print()
        i = getch()
        if i == r[0]:
            if mistakeCount == 0:
                r[2] += 1
            if mistakeCount > 0:
                r[2] = 0
            if r[2] > 2:
                l.remove(r)
            if len(l)==1:
                os.system('clear')
                print("GAME OVER")
                print("Your time:", round(time.time()-startGameTime, 2), "s")
                time.sleep(1)
                exit()
            break
        if i == "`":
            exit()
        if i != r[0]:
            mistakeCount += 1
