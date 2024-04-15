#!/bin/python3

import time
import pynput
import threading
import queue
import fcntl
import struct
import subprocess as sp

def loadDeviceList(): 
    deviceList = []
    output = sp.getoutput("ls /dev/input/event*")
    for x in output.splitlines():
        deviceList.append([x])
    for x in deviceList:
        name = sp.getoutput("cat /sys/class/input/"+x[0][11:]+"/device/name")
        x.append(name)
    deviceList.sort(key=lambda x: int(x[0][16:]))
    for x in deviceList: print(x[0], x[1])
    return deviceList

def loadConfigFiles():
    mouseName = ""
    keyboardName = ""
    try:
        with open("setting_mouse","r") as f:
            mouseName = f.readline().strip()
    except:
        print("no mouse file")
    try:
        with open("setting_keyboard","r") as f:
            keyboardName = f.readline().strip()
    except:
        print("no keyboard file")
    print("mouseName:", mouseName)
    print("keyboardName:", keyboardName)
    return mouseName, keyboardName

def findConfiguredDevices(mouseName, keyboardName, deviceList):
    mousePath = ""
    keyboardPath = ""
    for x in deviceList:
        if x[1] == mouseName:
            mousePath=x[0]
            break
    for x in deviceList:
        if x[1] == keyboardName:
            keyboardPath=x[0]
            break
    print("mousePath:", mousePath)
    print("keyboardPath:", keyboardPath)
    return mousePath, keyboardPath

def write(char123):
    keyboard.tap(char123)

def writeChar(char123):
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))

def writeCharUp(char123):
    keyboard.press(pynput.keyboard.Key.shift)
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.release(pynput.keyboard.Key.shift)

alt_gr_fix = 65027
def writeCharAltGr(char123):
    keyboard.press(pynput.keyboard.KeyCode(alt_gr_fix))
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.release(pynput.keyboard.KeyCode(alt_gr_fix))

def writeCharAltGrUp(char123):
    keyboard.press(pynput.keyboard.Key.shift)
    keyboard.press(pynput.keyboard.KeyCode(alt_gr_fix))
    keyboard.tap(pynput.keyboard.KeyCode(ord(char123)))
    keyboard.press(pynput.keyboard.KeyCode(alt_gr_fix))
    keyboard.release(pynput.keyboard.Key.shift)

#Mouse path
def readMouse():
    with open(mousePath, "rb") as file:
        EVIOCGRAB = 0x40044590
        try:
            fcntl.ioctl(file, EVIOCGRAB, 1)
            event_format = 'qqHHi'
            event_size = struct.calcsize(event_format)
            while True:
                event_data = file.read(event_size)
                (tv_sec, tv_usec, type, code, value) = struct.unpack(event_format, event_data)
                if type == 2 and (code == 0 or code == 1):
                    if(mouseActiveFlag):
                        mouseEvents.put([type, code, value])
        finally:
            fcntl.ioctl(file, EVIOCGRAB, 0)

def moveMouse():
    moveMouseTime = 0
    mouseDeltaX = 0
    mouseDeltaY = 0
    while True:
        mEvent = mouseEvents.get()
        if mEvent[1] == 0:
            mouseDeltaX += mEvent[2]
        elif mEvent[1] == 1:
            mouseDeltaY += mEvent[2]
        if time.time() - moveMouseTime > 0.005:
            mouse.move(mouseDeltaX, mouseDeltaY)
            mouseDeltaX = 0
            mouseDeltaY = 0
            moveMouseTime = time.time()

#Keyboard path
def readKeyboard():
    with open(keyboardPath, "rb") as file:
        EVIOCGRAB = 0x40044590
        try:
            fcntl.ioctl(file, EVIOCGRAB, 1)
            event_format = 'qqHHi'
            event_size = struct.calcsize(event_format)
            while True:
                event_data = file.read(event_size)
                (tv_sec, tv_usec, type, code, value) = struct.unpack(event_format, event_data)
                if type == 1 and (code == 19 or code == 20 or code == 21 or code == 22 or code == 57) and value != 2:
                    if keyboardM1Flag: keyboardEventsM1.put([type, code, value])
                    elif keyboardM2Flag: keyboardEventsM2.put([type, code, value])
        finally:
            fcntl.ioctl(file, EVIOCGRAB, 0)

#M1 path
def keyboardM1():
    flags = { 1: False,
            2: False,
            4: False,
            8: False,
            16: False }
    cflags = { 1: False,
            2: False,
            4: False ,
            8: False,
            16: False }

    while True:
        kEvent = keyboardEventsM1.get()

        if kEvent[1] == 57 and kEvent[2] == 1:
            flags[1] = True
            cflags[1] = True
        elif kEvent[1] == 22 and kEvent[2] == 1:
            flags[2] = True
            cflags[2] = True
        elif kEvent[1] == 21 and kEvent[2] == 1:
            flags[4] = True
            cflags[4] = True
        elif kEvent[1] == 20 and kEvent[2] == 1:
            flags[8] = True
            cflags[8] = True
        elif kEvent[1] == 19 and kEvent[2] == 1:
            flags[16] = True
            cflags[16] = True

        elif kEvent[1] == 57 and kEvent[2] == 0:
            cflags[1] = False
        elif kEvent[1] == 22 and kEvent[2] == 0:
            cflags[2] = False
        elif kEvent[1] == 21 and kEvent[2] == 0:
            cflags[4] = False
        elif kEvent[1] == 20 and kEvent[2] == 0:
            cflags[8] = False
        elif kEvent[1] == 19 and kEvent[2] == 0:
            cflags[16] = False
        
        if any(flags.values()) and not any(cflags.values()):
            output = flags[1]*1 + flags[2]*2 + flags[4]*4 + flags[8]*8 + flags[16]*16
            for x in flags:
                flags[x] = False
            keyboardSignalsM1Raw.put(output)

def keyboardRawToHexM1():
    xtime = 0
    sendString = "0"
    sendFlag = False
    while True:
        kEvent = keyboardSignalsM1Raw.get()
        if time.time() - xtime > 1:
            sendString = "0"
        xtime = time.time()

        if kEvent == 3: sendString = "1"
        elif kEvent == 5: sendString = "2"
        elif kEvent == 9: sendString = "3"
        elif kEvent == 17: sendString = "4"
        elif kEvent == 7: sendString = "5"
        elif kEvent == 13: sendString = "6"
        elif kEvent == 25: sendString = "7"
        elif kEvent == 15: sendString = "8"
        elif kEvent == 29: sendString = "9"
        elif kEvent == 31: sendString = "A"
        elif kEvent == 11: sendString = "B"
        elif kEvent == 21: sendString = "C"
        elif kEvent == 19: sendString = "D"
        elif kEvent == 23: sendString = "E"
        elif kEvent == 27: sendString = "F"

        elif kEvent == 1: sendString += "0" ; sendFlag = True
        elif kEvent == 2: sendString += "1" ; sendFlag = True
        elif kEvent == 4: sendString += "2" ; sendFlag = True
        elif kEvent == 8: sendString += "3" ; sendFlag = True
        elif kEvent == 16: sendString += "4" ; sendFlag = True
        elif kEvent == 6: sendString += "5" ; sendFlag = True
        elif kEvent == 12: sendString += "6" ; sendFlag = True
        elif kEvent == 24: sendString += "7" ; sendFlag = True
        elif kEvent == 14: sendString += "8" ; sendFlag = True
        elif kEvent == 28: sendString += "9" ; sendFlag = True
        elif kEvent == 30: sendString += "A" ; sendFlag = True
        elif kEvent == 10: sendString += "B" ; sendFlag = True
        elif kEvent == 20: sendString += "C" ; sendFlag = True
        elif kEvent == 18: sendString += "D" ; sendFlag = True
        elif kEvent == 22: sendString += "E" ; sendFlag = True
        elif kEvent == 26: sendString += "F" ; sendFlag = True
        
        if sendFlag:
            keyboardSignalsM1.put(sendString)
            sendString = "0"
            sendFlag = False

def keyboardM1Actions():
    while True:
        x = keyboardSignalsM1.get()
        if x == "00": write(pynput.keyboard.Key.space)
        elif x == "01": writeChar('a')
        elif x == "02": writeChar('i')
        elif x == "03": writeChar('e')
        elif x == "04": write(pynput.keyboard.Key.backspace)
        elif x == "05": writeChar('o')
        elif x == "06": writeChar('z')
        elif x == "07": writeChar('n')
        elif x == "08": writeChar('r')
        elif x == "09": writeChar('w')
        elif x == "0A": writeChar('s')
        elif x == "0B": writeChar('c')
        elif x == "0C": writeChar('t')
        elif x == "0D": writeChar('y')
        elif x == "0E": writeChar('k')
        elif x == "0F": writeChar('d')
    ####
        elif x == "10": writeCharUp('-')
        elif x == "11": writeCharUp('a')
        elif x == "12": writeCharUp('i')
        elif x == "13": writeCharUp('e')
        elif x == "14": write(pynput.keyboard.Key.delete)
        elif x == "15": writeCharUp('o')
        elif x == "16": writeCharUp('z')
        elif x == "17": writeCharUp('n')
        elif x == "18": writeCharUp('r')
        elif x == "19": writeCharUp('w')
        elif x == "1A": writeCharUp('s')
        elif x == "1B": writeCharUp('c')
        elif x == "1C": writeCharUp('t')
        elif x == "1D": writeCharUp('y')
        elif x == "1E": writeCharUp('k')
        elif x == "1F": writeCharUp('d')
    ####
        elif x == "20": writeChar('h')
        elif x == "21": writeChar('l')
        elif x == "22": writeChar('u')
        elif x == "23": writeChar('m')
        elif x == "24": writeChar('f')
        elif x == "25": writeChar('g')
        elif x == "26": writeChar('p')
        elif x == "27": writeChar('b')
        elif x == "28": writeChar('v')
        elif x == "29": writeChar('j')
        elif x == "2A": writeChar('x')
        elif x == "2B": writeChar('q')
        elif x == "2C": writeCharUp('0')
        elif x == "2D": writeChar(']')
        elif x == "2E": writeCharUp(']')
        elif x == "2F": writeCharUp('.')
    ####
        elif x == "30": writeCharUp('h')
        elif x == "31": writeCharUp('l')
        elif x == "32": writeCharUp('u')
        elif x == "33": writeCharUp('m')
        elif x == "34": writeCharUp('f')
        elif x == "35": writeCharUp('g')
        elif x == "36": writeCharUp('p')
        elif x == "37": writeCharUp('b')
        elif x == "38": writeCharUp('v')
        elif x == "39": writeCharUp('j')
        elif x == "3A": writeCharUp('x')
        elif x == "3B": writeCharUp('q')
        elif x == "3C": writeCharUp('9')
        elif x == "3D": writeChar('[')
        elif x == "3E": writeCharUp('[')
        elif x == "3F": writeCharUp(',')
    ####
        elif x == "40": writeChar('0')
        elif x == "41": writeChar('1')
        elif x == "42": writeChar('2')
        elif x == "43": writeChar('3')
        elif x == "44": changeToMouse()
        elif x == "45": writeChar('5')
        elif x == "46": writeChar('6')
        elif x == "47": writeChar('7')
        elif x == "48": writeChar('8')
        elif x == "49": writeChar('9')
        elif x == "4A": writeCharUp('=')
        elif x == "4B": writeChar('-')
        elif x == "4C": writeCharUp('8')
        elif x == "4D": writeChar('/')
        elif x == "4E": writeCharUp('6')
        elif x == "4F": writeChar('=')
    ####
        elif x == "50": write(pynput.keyboard.Key.tab)
        elif x == "51": writeChar('.')
        elif x == "52": writeChar(',')
        elif x == "53": writeCharUp(';')
        elif x == "54": writeChar(';')
        elif x == "55": writeChar("'")
        elif x == "56": writeCharUp("'")
        elif x == "57": writeChar("\\")
        elif x == "58": writeCharUp("\\")
        elif x == "59": writeCharUp("/")
        elif x == "5A": writeCharUp('1')
        elif x == "5B": writeCharUp('2')
        elif x == "5C": writeCharUp('3')
        elif x == "5D": writeCharUp('4')
        elif x == "5E": writeCharUp('5')
        elif x == "5F": writeCharUp('7')
    ####
        elif x == "61": writeCharAltGr("a")
        elif x == "62": writeCharAltGr("l")
        elif x == "63": writeCharAltGr("e")
        elif x == "65": writeCharAltGr("o")
        elif x == "66": writeCharAltGr("z")
        elif x == "67": writeCharAltGr("n")
        elif x == "68": writeCharAltGr("x")
        elif x == "6A": writeCharAltGr("s")
        elif x == "6B": writeCharAltGr("c")
    ####
        elif x == "71": writeCharAltGrUp("a")
        elif x == "72": writeCharAltGrUp("l")
        elif x == "73": writeCharAltGrUp("e")
        elif x == "75": writeCharAltGrUp("o")
        elif x == "76": writeCharAltGrUp("z")
        elif x == "77": writeCharAltGrUp("n")
        elif x == "78": writeCharAltGrUp("x")
        elif x == "7A": writeCharAltGrUp("s")
        elif x == "7B": writeCharAltGrUp("c")
    ####
        elif x == "80": write(pynput.keyboard.Key.enter)
        elif x == "81": write(pynput.keyboard.Key.f1)
        elif x == "82": write(pynput.keyboard.Key.f2)
        elif x == "83": write(pynput.keyboard.Key.f3)
        elif x == "84": write(pynput.keyboard.Key.f4)
        elif x == "85": write(pynput.keyboard.Key.f5)
        elif x == "86": write(pynput.keyboard.Key.f6)
        elif x == "87": write(pynput.keyboard.Key.f7)
        elif x == "88": write(pynput.keyboard.Key.f8)
        elif x == "89": write(pynput.keyboard.Key.f9)
        elif x == "8A": write(pynput.keyboard.Key.f10)
        elif x == "8B": write(pynput.keyboard.Key.f11)
        elif x == "8C": write(pynput.keyboard.Key.f12)
        elif x == "8D": write(pynput.keyboard.Key.esc)
        elif x == "8E": writeCharUp('`')
        elif x == "8F": writeChar('`')
    ####
        elif x == "E0": write(pynput.keyboard.Key.down)
        elif x == "E1": write(pynput.keyboard.Key.up)
        elif x == "ED": pass
        elif x == "EE": break
        elif x == "EF": time.sleep(10)
        print(x)

#M2 path
def keyboardM2():
    flags = { 1: False,
            8: False,
            16: False }
    cflags = { 1: False,
            8: False,
            16: False }

    while True:
        kEvent = keyboardEventsM2.get()
        if kEvent[1] == 22: #U key
            if kEvent[2] == 0: # key up
                keyboardSignalsM2.put("01_R") # Key 1 realise
            elif kEvent[2] == 1: # key down
                keyboardSignalsM2.put("01_P") # Key 1 press
        elif kEvent[1] == 21: # Y key
            if kEvent[2] == 0:
                keyboardSignalsM2.put("02_R")
            elif kEvent[2] == 1:
                keyboardSignalsM2.put("02_P")

        elif kEvent[1] == 57 and kEvent[2] == 1:
            flags[1] = True
            cflags[1] = True
        elif kEvent[1] == 20 and kEvent[2] == 1:
            flags[8] = True
            cflags[8] = True
        elif kEvent[1] == 19 and kEvent[2] == 1:
            flags[16] = True
            cflags[16] = True

        elif kEvent[1] == 57 and kEvent[2] == 0:
            cflags[1] = False
        elif kEvent[1] == 20 and kEvent[2] == 0:
            cflags[8] = False
        elif kEvent[1] == 19 and kEvent[2] == 0:
            cflags[16] = False
        
        if any(flags.values()) and not any(cflags.values()):
            output = flags[1]*1 + flags[8]*8 + flags[16]*16
            for x in flags:
                flags[x] = False
            keyboardSignalsM2Raw.put(output)

def keyboardRawToHexM2():
    xtime = 0
    sendString = "0"
    sendFlag = False
    while True:
        kEvent = keyboardSignalsM2Raw.get()
        if time.time() - xtime > 1:
            sendString = "0"
        xtime = time.time()

        if kEvent == 9: sendString = "3"
        elif kEvent == 17: sendString = "4"
        elif kEvent == 25: sendString = "7"

        elif kEvent == 1: sendString += "0" ; sendFlag = True
        elif kEvent == 8: sendString += "3" ; sendFlag = True
        elif kEvent == 16: sendString += "4" ; sendFlag = True
        elif kEvent == 24: sendString += "7" ; sendFlag = True

        if sendFlag:
            keyboardSignalsM2.put(sendString)
            sendString = "0"
            sendFlag = False

def keyboardM2Actions():
    while True:
        x = keyboardSignalsM2.get()
        if x == "01_P": mouse.press(pynput.mouse.Button.left)
        elif x == "01_R": mouse.release(pynput.mouse.Button.left)
        elif x == "02_P": mouse.press(pynput.mouse.Button.right)
        elif x == "02_R": mouse.release(pynput.mouse.Button.right)
        elif x == "03": mouse.scroll(0, -1)
        elif x == "04": mouse.scroll(0, 1)
        elif x == "44": changeToKeyboard()
        print(x)

def changeToKeyboard():
    global mouseActiveFlag
    global keyboardM2Flag
    global keyboardM1Flag
    global mousePosition

    mousePosition = mouse.position
    mouse.position = (10000,10000)

    mouseActiveFlag = False
    keyboardM2Flag = False
    keyboardM1Flag = True

def changeToMouse():
    global mouseActiveFlag
    global keyboardM2Flag
    global keyboardM1Flag
    global mousePosition

    mouse.position = mousePosition

    keyboardM1Flag = False
    keyboardM2Flag = True
    mouseActiveFlag = True

# Program START
mousePosition = None

l = loadDeviceList()
m,k = loadConfigFiles()
mousePath, keyboardPath = findConfiguredDevices(m,k,l)
if not mousePath or not keyboardPath:
    print("no path to device, program exit")
    exit()



mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
keyboard.release(pynput.keyboard.Key.enter)

changeToKeyboard()

# Mouse
mouseThread = threading.Thread(target=readMouse)
mouseEvents = queue.Queue()
moveMouseThread = threading.Thread(target=moveMouse)

# Keyboard
keyboardThread = threading.Thread(target=readKeyboard)
keyboardEventsM1 = queue.Queue()
keyboardEventsM2 = queue.Queue()

# M1
keyboardM1Thread = threading.Thread(target=keyboardM1)
keyboardSignalsM1Raw = queue.Queue()
keyboardSignalsM1 = queue.Queue()
keyboardRawToHexM1Thread = threading.Thread(target=keyboardRawToHexM1)
keyboardM1ActionsThread = threading.Thread(target=keyboardM1Actions)

# M2
keyboardM2Thread = threading.Thread(target=keyboardM2)
keyboardSignalsM2Raw = queue.Queue()
keyboardSignalsM2 = queue.Queue()
keyboardRawToHexM2Thread = threading.Thread(target=keyboardRawToHexM2)
keyboardM2ActionsThread = threading.Thread(target=keyboardM2Actions)

mouseThread.daemon = True
moveMouseThread.daemon = True

keyboardThread.daemon = True

keyboardM1Thread.daemon = True
keyboardRawToHexM1Thread.daemon = True
keyboardM1ActionsThread.daemon = True

keyboardM2Thread.daemon = True
keyboardRawToHexM2Thread.daemon = True
keyboardM2ActionsThread.daemon = True

mouseThread.start()
moveMouseThread.start()

keyboardThread.start()

keyboardM1Thread.start()
keyboardRawToHexM1Thread.start()
keyboardM1ActionsThread.start()

keyboardM2Thread.start()
keyboardRawToHexM2Thread.start()
keyboardM2ActionsThread.start()

keyboardM1ActionsThread.join()