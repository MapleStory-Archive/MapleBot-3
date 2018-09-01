import pyautogui
import time

time.sleep(3)

start_buff_bless = time.time()

delay_buff_bless = 100


def up():
    time.sleep(3)
    pyautogui.keyDown('up')
    pyautogui.keyDown('f')
    time.sleep(0.5)
    pyautogui.keyUp('f')
    pyautogui.keyUp('up')
    time.sleep(0.5)

def down():
    time.sleep(3)
    pyautogui.keyDown('down')
    pyautogui.keyDown('f')
    time.sleep(0.5)
    pyautogui.keyUp('f')
    pyautogui.keyUp('down')
    time.sleep(0.5)


def hit():
    pyautogui.keyDown('d')
    time.sleep(7)
    pyautogui.keyUp('d')
    pyautogui.press('ctrlright')

def left():
    pyautogui.keyDown('left')
    time.sleep(0.06)
    pyautogui.keyUp('left')
    time.sleep(1)

def right():
    pyautogui.keyDown('right')
    time.sleep(0.06)
    pyautogui.keyUp('right')
    time.sleep(1)

while True:
    hit()
    hit()
    up()
    hit()
    hit()
    down()
    right()
    left()
    if time.time() > start_buff_bless + delay_buff_bless:
        time.sleep(1)
        pyautogui.press('home')
        pyautogui.press('home')
        pyautogui.press('home')
        time.sleep(4)
        start_buff_bless = time.time()
