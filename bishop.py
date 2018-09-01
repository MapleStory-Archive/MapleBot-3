import pyautogui
import time

time.sleep(3)

start_buff_bless = time.time()
start_feed = time.time()
delay_buff_bless = 100
delay_feed = 1800


def hit():
    pyautogui.keyDown('d')
    time.sleep(7)
    pyautogui.keyUp('d')
    pyautogui.press('ctrlright')


def left():
	time.sleep(3)
	pyautogui.keyDown('left')
	time.sleep(0.06)
	pyautogui.keyUp('left')
	time.sleep(1)

#walks shorter to the right than to the left..
def right():
	time.sleep(3)
	pyautogui.keyDown('right')
	time.sleep(0.059)
	pyautogui.keyUp('right')
	time.sleep(1)


while True:
	left()
	hit()
	right()
	hit()
	if time.time() > start_buff_bless + delay_buff_bless:
		time.sleep(1)
		if time.time() > start_feed + delay_feed:
			pyautogui.press('pageup')
			start_feed = time.time()
		pyautogui.press('home')
		pyautogui.press('home')
		pyautogui.press('home')
		time.sleep(4)
		start_buff_bless = time.time()
