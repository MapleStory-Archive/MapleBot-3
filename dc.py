import pyautogui
import time
import _thread
import sys
from action import *

start_buff_1 = time.time()
start_cycle = time.time()
start_feed = time.time()
delay_buff_1 = 1
delay_cycle = 150
delay_feed = 600


def check_buff_1():
    global start_buff_1
    if time.time() > start_buff_1 + delay_buff_1:
        time.sleep(1)
        pyautogui.press('1')
        pyautogui.press('1')
        pyautogui.press('1')
        time.sleep(1)
        pyautogui.press('4')
        pyautogui.press('4')
        pyautogui.press('4')
        time.sleep(1)
        pyautogui.press('2')
        pyautogui.press('2')
        pyautogui.press('2')
        time.sleep(1)
        start_buff_1 = time.time()


def feed_my_pig():
    global start_feed
    if time.time() > start_feed + delay_feed:
        pyautogui.press('pageup')
        start_feed = time.time()


def positioning_C1(x1, x2):
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    while not x1 <= position[0] <= x2:
        if position[0] < x1:
            tele_right()
        elif position[0] > x2:
            pyautogui.keyDown('left')
            pyautogui.keyDown('f')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
        pyautogui.keyUp('left')
        pyautogui.keyUp('f')


def positioning_T1(x1):
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    while not position[0] <= x1:
        pyautogui.keyDown('left')
        pyautogui.keyDown('f')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
    pyautogui.keyUp('left')
    pyautogui.keyUp('f')


def positioning_C2(x1, x2):
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    while not position[0] >= x1:
        pyautogui.keyDown('right')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
    while not position[0] >= x2:
        pyautogui.keyDown('space')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
    pyautogui.keyUp('right')
    pyautogui.keyUp('space')


def positioning_C3():
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    if position[1] > 274 or position[1] < 268:
        print('platform position check failed')
        print(position[1])
        return False
    elif position[0] > 283:
        print('platform position check semi-failed, rectifying')
        pyautogui.keyDown('left')
        time.sleep(0.7)
        pyautogui.keyUp('left')
    return True


def loot():
    print('Alert: looting starts')
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    while not position[1] > 290:
        pyautogui.keyDown('down')
        pyautogui.keyDown('f')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
    pyautogui.keyUp('f')
    pyautogui.keyUp('down')
    positioning_C2(230, 257)
    # Buff
    check_buff_1()
    feed_my_pig()
    # Reposition on platform
    posi_check = positioning_C3()
    if posi_check is False:
        return
    # Selling
    selling()
    # Kill a wave
    pyautogui.press('d')
    time.sleep(4)
    pyautogui.press('d')
    time.sleep(4)
    pyautogui.press('d')
    time.sleep(4)
    pyautogui.press('d')
    time.sleep(4)
    # Tele up
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    pyautogui.keyDown('up')
    pyautogui.keyDown('f')
    time.sleep(2.7)
    pyautogui.keyUp('up')
    pyautogui.keyUp('f')


def selling():
	print('Selling loots...')
	pyautogui.doubleClick(x=646, y=255)
	position = pyautogui.locateCenterOnScreen(
        './data/shop.png', region=(1076, 368, 90, 50))
	while position is not None:
	    pyautogui.doubleClick(x=645, y=157)
	    time.sleep(1)
	pyautogui.click(x=442, y=363, clicks=30, interval=0.25)
	position = pyautogui.locateCenterOnScreen(
	    './data/areyousure.png', region=(614, 594, 364, 44))
	if position is not None:
	    pyautogui.press('esc')
	pyautogui.click(x=348, y=179)


def positioning_T2(x1):
    position = pyautogui.locateCenterOnScreen(
        './data/self.png', region=(0, 0, 400, 400))
    while not position[0] < x1:
        pyautogui.keyDown('left')
        position = pyautogui.locateCenterOnScreen(
            './data/self.png', region=(0, 0, 400, 400))
    pyautogui.keyUp('left')
    print('Alert: looting ends')


def check_alert():
    while pyautogui.locateOnScreen('./data/0hp.png', region=(437, 1208, 213, 32), grayscale=True):
        sys.stdout.write('\a')
        sys.stdout.flush()


### potting thread ###
_thread.start_new_thread(potting, ())

### main process ###
while True:
    # C1
    while not time.time() > start_cycle + delay_cycle:
        positioning_C1(140, 196)
        hit()
    # T1
    print('T1 in process')
    positioning_T1(140)
    # C2
    loot()
    # T2
    print('T2 in process')
    positioning_T2(110)
    start_cycle = time.time()
