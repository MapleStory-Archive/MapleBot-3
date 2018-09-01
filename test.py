import pyautogui 
import time

time.sleep(3)

start_buff_bless = time.time()
start_walkback = time.time()
start_hardattack = time.time()
start_walkright = time.time()
start_buff_invin = time.time()
delay_buff_bless = 15
delay_buff_invin = 30
delay_walkback = 6
delay_walkright = 13
# delay_hardattack = 2

while True:
	pyautogui.keyDown('s')
	print('attacking(heal)...')
	# if time.time() > start_hardattack + delay_hardattack : 
	# 	pyautogui.press('d')
	# 	pyautogui.press('d')
	# 	pyautogui.press('d')
	# 	start_hardattack = time.time()
	if time.time() > start_buff_bless + delay_buff_bless : 
		pyautogui.press('2')
		pyautogui.press('2')
		start_buff_bless = time.time()
	if time.time() > start_buff_invin + delay_buff_invin : 
		pyautogui.press('4')
		pyautogui.press('4')
		start_buff_invin = time.time()
	if time.time() > start_walkback + delay_walkback : 
		pyautogui.keyUp('s')	
		pyautogui.keyDown('left')
		pyautogui.press('f')
		pyautogui.press('f')
		pyautogui.keyUp('left')	
		pyautogui.keyDown('s')
		start_walkback = time.time()
	if time.time() > start_walkright + delay_walkright : 
		pyautogui.keyUp('s')
		pyautogui.keyDown('right')
		pyautogui.press('f')
		pyautogui.press('f')
		pyautogui.keyUp('right')
		pyautogui.keyDown('s')
		start_walkright = time.time()

