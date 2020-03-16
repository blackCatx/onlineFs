import pyautogui
import time
import random
import win32gui
import win32api


def handler(hwnd, windows):
    windows.append((hwnd, win32gui.GetWindowText(hwnd)))


all_windows = []
wow_windows = []
win32gui.EnumWindows(handler, all_windows)
for i in all_windows:
    if "魔兽世界" in i[1]: 
        wow_windows.append(i[0])


def send_keypress(hwnd, key):
    win32gui.SendMessage(hwnd, 0x0100, key, 0)
    win32gui.SendMessage(hwnd, 0x0101, key, 0)



while True:
	if win32api.GetKeyState(0x32) < 0:
		for i in wow_windows:
			send_keypress(i, 0x32)

	if win32api.GetKeyState(0x31) < 0:
		for i in wow_windows:
			send_keypress(i, 0x31)	
	if win32api.GetKeyState(0x33) < 0:
		for i in wow_windows:
			send_keypress(i, 0x33)	
	if win32api.GetKeyState(0x34) < 0:
		for i in wow_windows:
			send_keypress(i, 0x34)	
	if win32api.GetKeyState(0x35) < 0:
		for i in wow_windows:
			send_keypress(i, 0x35)	
	if win32api.GetKeyState(0x36) < 0:
		for i in wow_windows:
			send_keypress(i, 0x36)	
