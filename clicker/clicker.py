import pyautogui
import time
import math
import datetime
from getkey import getkey
import pyautogui
import os
from playsound import playsound

#interface config
y000p = 1030 # power 0%
y100p = 945 # power 100%

yl = list()  # y list
for x in range(101):
    step = (y000p-y100p)/100
    yv =int(y000p-x*step)  # y value
    yl.append(yv)

def power(x, t=0.2):
    pyautogui.click(180, yl[x])
    time.sleep(t)

def buy(x, t=0.2):
    for _ in range(x):
        pyautogui.click(1500, 1140)
        time.sleep(t)

def lin(p1, p2, t):
    tStepN = int(t/0.3)
    print(tStepN)
    pStep = (p2-p1)/tStepN
    print(pStep)
    for x in range(tStepN):
        p = int(p1+x*pStep)
        print(p)
        power(p , 0.2)

os.system('clear')
b = ""
while True:
    b += getkey()

    if "e" in b: 
        b = ""
        buy(2)
        
        lin(20,90,18)
        #power(90)

