import pyautogui
import time

def hit():
    pyautogui.keyDown('d')
    time.sleep(3)
    pyautogui.keyUp('d')


def check_hp():
    while not pyautogui.locateOnScreen('./data/hp.png', region=(436, 1206, 130, 36), grayscale=True):
        print('Action: hp potting')
        pyautogui.press('home')
        time.sleep(0.5)


def check_mp():
    while not pyautogui.locateOnScreen('./data/mp.png', region=(650, 1206, 86, 38), grayscale=True):
        print('Action: mp potting')
        pyautogui.press('home')
        time.sleep(0.5)


def potting():
    while True:
        check_mp()
        check_hp()

def tele_left():
    pyautogui.keyDown('left')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.keyUp('left')


def tele_right():
    pyautogui.keyDown('right')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.keyUp('right')


def tele_down():
    pyautogui.keyDown('down')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.keyUp('down')


def tele_up():
    pyautogui.keyDown('up')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.keyUp('up')
