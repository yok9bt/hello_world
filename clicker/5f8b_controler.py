#!/bin/python3

import time
import os
import pynput

flag1 = 0
flag2 = 0
flag4 = 0
flag8 = 0
flag16 = 0
highhex = "0"
hightime = 0
keyboard = pynput.keyboard.Controller()
km = os.popen('sudo /home/adrian/hello_world/clicker/evtest.sh')
keyboard.release(pynput.keyboard.Key.enter)

def write(char123):
    keyboard.tap(char123)

def writeChar(char123):
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))

def writeCharUp(char123):
    keyboard.press(pynput.keyboard.Key.shift)
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.release(pynput.keyboard.Key.shift)

def writeCharAltGr(char123):
    keyboard.press(pynput.keyboard.Key.alt_gr)
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.release(pynput.keyboard.Key.alt_gr)

def writeCharAltGrUp(char123):
    keyboard.press(pynput.keyboard.Key.shift)
    keyboard.press(pynput.keyboard.Key.alt_gr)
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.release(pynput.keyboard.Key.alt_gr)
    keyboard.release(pynput.keyboard.Key.shift)

def sendSymbol(symbol):
    print('<'+symbol+'>')
    if symbol == "00":
        write(pynput.keyboard.Key.space)
    elif symbol == "01":
        writeChar('a')
    elif symbol == "02":
        writeChar('i')
    elif symbol == "03":
        writeChar('e')
    elif symbol == "04":
        write(pynput.keyboard.Key.backspace)
    elif symbol == "05":
        writeChar('o')
    elif symbol == "06":
        writeChar('z')
    elif symbol == "07":
        writeChar('n')
    elif symbol == "08":
        writeChar('r')
    elif symbol == "09":
        writeChar('w')
    elif symbol == "0A":
        writeChar('s')
    elif symbol == "0B":
        writeChar('c')
    elif symbol == "0C":
        writeChar('t')
    elif symbol == "0D":
        writeChar('y')
    elif symbol == "0E":
        writeChar('k')
    elif symbol == "0F":
        writeChar('d')
####
    elif symbol == "10":
        writeCharUp('-')
    elif symbol == "11":
        writeCharUp('a')
    elif symbol == "12":
        writeCharUp('i')
    elif symbol == "13":
        writeCharUp('e')
    elif symbol == "14":
        write(pynput.keyboard.Key.delete)
    elif symbol == "15":
        writeCharUp('o')
    elif symbol == "16":
        writeCharUp('z')
    elif symbol == "17":
        writeCharUp('n')
    elif symbol == "18":
        writeCharUp('r')
    elif symbol == "19":
        writeCharUp('w')
    elif symbol == "1A":
        writeCharUp('s')
    elif symbol == "1B":
        writeCharUp('c')
    elif symbol == "1C":
        writeCharUp('t')
    elif symbol == "1D":
        writeCharUp('y')
    elif symbol == "1E":
        writeCharUp('k')
    elif symbol == "1F":
        writeCharUp('d')
####
    elif symbol == "20":
        writeChar('h')
    elif symbol == "21":
        writeChar('l')
    elif symbol == "22":
        writeChar('u')
    elif symbol == "23":
        writeChar('m')
    elif symbol == "24":
        writeChar('f')
    elif symbol == "25":
        writeChar('g')
    elif symbol == "26":
        writeChar('p')
    elif symbol == "27":
        writeChar('b')
    elif symbol == "28":
        writeChar('v')
    elif symbol == "29":
        writeChar('j')
    elif symbol == "2A":
        writeChar('x')
    elif symbol == "2B":
        writeChar('q')
    elif symbol == "2C":
        writeCharUp('0')
    elif symbol == "2D":
        writeChar(']')
    elif symbol == "2E":
        writeCharUp(']')
    elif symbol == "2F":
        writeCharUp('.')
####
    elif symbol == "30":
        writeCharUp('h')
    elif symbol == "31":
        writeCharUp('l')
    elif symbol == "32":
        writeCharUp('u')
    elif symbol == "33":
        writeCharUp('m')
    elif symbol == "34":
        writeCharUp('f')
    elif symbol == "35":
        writeCharUp('g')
    elif symbol == "36":
        writeCharUp('p')
    elif symbol == "37":
        writeCharUp('b')
    elif symbol == "38":
        writeCharUp('v')
    elif symbol == "39":
        writeCharUp('j')
    elif symbol == "3A":
        writeCharUp('x')
    elif symbol == "3B":
        writeCharUp('q')
    elif symbol == "3C":
        writeCharUp('9')
    elif symbol == "3D":
        writeChar('[')
    elif symbol == "3E":
        writeCharUp('[')
    elif symbol == "3F":
        writeCharUp(',')
####
    elif symbol == "40":
        writeChar('0')
    elif symbol == "41":
        writeChar('1')
    elif symbol == "42":
        writeChar('2')
    elif symbol == "43":
        writeChar('3')
    elif symbol == "44":
        writeChar('4')
    elif symbol == "45":
        writeChar('5')
    elif symbol == "46":
        writeChar('6')
    elif symbol == "47":
        writeChar('7')
    elif symbol == "48":
        writeChar('8')
    elif symbol == "49":
        writeChar('9')
    elif symbol == "4A":
        writeCharUp('=')
    elif symbol == "4B":
        writeChar('-')
    elif symbol == "4C":
        writeCharUp('8')
    elif symbol == "4D":
        writeChar('/')
    elif symbol == "4E":
        writeCharUp('6')
    elif symbol == "4F":
        writeChar('=')
####
    elif symbol == "50":
        write(pynput.keyboard.Key.tab)
    elif symbol == "51":
        writeChar('.')
    elif symbol == "52":
        writeChar(',')
    elif symbol == "53":
        writeCharUp(';')
    elif symbol == "54":
        writeChar(';')
    elif symbol == "55":
        writeChar("'")
    elif symbol == "56":
        writeCharUp("'")
    elif symbol == "57":
        writeChar("\\")
    elif symbol == "58":
        writeCharUp("\\")
    elif symbol == "59":
        writeCharUp("/")
    elif symbol == "5A":
        writeCharUp('1')
    elif symbol == "5B":
        writeCharUp('2')
    elif symbol == "5C":
        writeCharUp('3')
    elif symbol == "5D":
        writeCharUp('4')
    elif symbol == "5E":
        writeCharUp('5')
    elif symbol == "5F":
        writeCharUp('7')
####
    elif symbol == "61":
        writeCharAltGr("a")
    elif symbol == "62":
        writeCharAltGr("l")
    elif symbol == "63":
        writeCharAltGr("e")
    elif symbol == "65":
        writeCharAltGr("o")
    elif symbol == "66":
        writeCharAltGr("z")
    elif symbol == "67":
        writeCharAltGr("n")
    elif symbol == "68":
        writeCharAltGr("x")
    elif symbol == "6A":
        writeCharAltGr("s")
    elif symbol == "6B":
        writeCharAltGr("c")
####
    elif symbol == "71":
        writeCharAltGrUp("a")
    elif symbol == "72":
        writeCharAltGrUp("l")
    elif symbol == "73":
        writeCharAltGrUp("e")
    elif symbol == "75":
        writeCharAltGrUp("o")
    elif symbol == "76":
        writeCharAltGrUp("z")
    elif symbol == "77":
        writeCharAltGrUp("n")
    elif symbol == "78":
        writeCharAltGrUp("x")
    elif symbol == "7A":
        writeCharAltGrUp("s")
    elif symbol == "7B":
        writeCharAltGrUp("c")
####
    elif symbol == "80":
        write(pynput.keyboard.Key.enter)
    elif symbol == "81":
        write(pynput.keyboard.Key.f1)
    elif symbol == "82":
        write(pynput.keyboard.Key.f2)
    elif symbol == "83":
        write(pynput.keyboard.Key.f3)
    elif symbol == "84":
        write(pynput.keyboard.Key.f4)
    elif symbol == "85":
        write(pynput.keyboard.Key.f5)
    elif symbol == "86":
        write(pynput.keyboard.Key.f6)
    elif symbol == "87":
        write(pynput.keyboard.Key.f7)
    elif symbol == "88":
        write(pynput.keyboard.Key.f8)
    elif symbol == "89":
        write(pynput.keyboard.Key.f9)
    elif symbol == "8A":
        write(pynput.keyboard.Key.f10)
    elif symbol == "8B":
        write(pynput.keyboard.Key.f11)
    elif symbol == "8C":
        write(pynput.keyboard.Key.f12)
    elif symbol == "8D":
        write(pynput.keyboard.Key.esc)
    elif symbol == "8E":
        writeCharUp('`')
    elif symbol == "8F":
        writeChar('`')
####
    elif symbol == "E0":
        write(pynput.keyboard.Key.down)
    elif symbol == "E1":
        write(pynput.keyboard.Key.up)
    elif symbol == "ED":
        volCtrl()
    elif symbol == "EE":
        exit()
    elif symbol == "EF":
        time.sleep(10)

def volCtrl():
    exitflag = 0
    while True:
        line123 = km.readline()
        if "value 1" in line123 and "(KEY_R)" in line123:
            exitflag = 1
        if "value 0" in line123 and "(KEY_R)" in line123:
            if exitflag == 1:
                break
        if "value 1" in line123 and "(KEY_Y)" in line123:
            write(pynput.keyboard.Key.media_volume_down)
        if "value 1" in line123 and "(KEY_U)" in line123:
            write(pynput.keyboard.Key.media_volume_up)

while True:
    line123 = km.readline()
    if any(x in line123 for x in ["(KEY_R)", "(KEY_T)", "(KEY_Y)", "(KEY_U)", "(KEY_SPACE)"]):
        if "value 1" in line123:
            if "(KEY_R)" in line123:
                flag16 = 1
            if "(KEY_T)" in line123:
                flag8 = 1
            if "(KEY_Y)" in line123:
                flag4 = 1
            if "(KEY_U)" in line123:
                flag2 = 1
            if "(KEY_SPACE)" in line123:
                flag1 = 1

        if "value 0" in line123:
            output = flag1*1 + flag2*2 + flag4*4 + flag8*8 + flag16*16
            if output>0:
                if (time.time()-hightime) > 1:
                    highhex = "0"

                if output == 1:
                    sendSymbol(highhex + "0")
                    highhex = "0"

                elif output == 2:
                    sendSymbol(highhex + "1")
                    highhex = "0"

                elif output == 4:
                    sendSymbol(highhex + "2")
                    highhex = "0"

                elif output == 8:
                    sendSymbol(highhex + "3")
                    highhex = "0"

                elif output == 16:
                    sendSymbol(highhex + "4")
                    highhex = "0"

                elif output == 6:
                    sendSymbol(highhex + "5")
                    highhex = "0"

                elif output == 12:
                    sendSymbol(highhex + "6")
                    highhex = "0"

                elif output == 24:
                    sendSymbol(highhex + "7")
                    highhex = "0"

                elif output == 14:
                    sendSymbol(highhex + "8")
                    highhex = "0"

                elif output == 28:
                    sendSymbol(highhex + "9")
                    highhex = "0"

                elif output == 30:
                    sendSymbol(highhex + "A")
                    highhex = "0"

                elif output == 10:
                    sendSymbol(highhex + "B")
                    highhex = "0"

                elif output == 20:
                    sendSymbol(highhex + "C")
                    highhex = "0"

                elif output == 18:
                    sendSymbol(highhex + "D")
                    highhex = "0"

                elif output == 22:
                    sendSymbol(highhex + "E")
                    highhex = "0"

                elif output == 26:
                    sendSymbol(highhex + "F")
                    highhex = "0"
                
                elif output == 3:
                    highhex = "1"
                    hightime = time.time()

                elif output == 5:
                    highhex = "2"
                    hightime = time.time()

                elif output == 9:
                    highhex = "3"
                    hightime = time.time()

                elif output == 17:
                    highhex = "4"
                    hightime = time.time()

                elif output == 7:
                    highhex = "5"
                    hightime = time.time()

                elif output == 13:
                    highhex = "6"
                    hightime = time.time()

                elif output == 25:
                    highhex = "7"
                    hightime = time.time()

                elif output == 15:
                    highhex = "8"
                    hightime = time.time()

                elif output == 29:
                    highhex = "9"
                    hightime = time.time()

                elif output == 31:
                    highhex = "A"
                    hightime = time.time()

                elif output == 11:
                    highhex = "B"
                    hightime = time.time()
                
                elif output == 21:
                    highhex = "C"
                    hightime = time.time()

                elif output == 19:
                    highhex = "D"
                    hightime = time.time()

                elif output == 23:
                    highhex = "E"
                    hightime = time.time()

                elif output == 27:
                    highhex = "F"
                    hightime = time.time()

            flag1 = 0
            flag2 = 0
            flag4 = 0
            flag8 = 0
            flag16 = 0
