import pyautogui
import time
import random
import win32gui


def handler(hwnd, windows):
    windows.append((hwnd, win32gui.GetWindowText(hwnd)))


all_windows = []
wow_windows = []
win32gui.EnumWindows(handler, all_windows)
for i in all_windows:
    if "魔兽世界" in i[1]: 
        wow_windows.append(i[0])


def switch_to_window(hwnd):
    win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
    win32gui.SetForegroundWindow(hwnd)


def logout_login():
    pyautogui.press('esc')
    time.sleep(5)
    pyautogui.click(960, 618)
    time.sleep(30)
    pyautogui.click(960, 988)
    time.sleep(30)


moves = [('w',), ('a',), ('s',), ('d',),
         ('w', 'a'), ('w', 'd'), ('s', 'a'), ('s', 'd')]


def send_keypress(hwnd, key):
    win32gui.SendMessage(hwnd, 0x0100, key, 0)
    win32gui.SendMessage(hwnd, 0x0101, key, 0)


def random_move():
    for i in range(random.randint(5, 8)):
        pyautogui.hotkey(*random.choice(moves),
                         interval=(0.2 + random.random() * 0.5))


time.sleep(10)
while True:
    for i in wow_windows:
        # switch_to_window(i)
        time.sleep(5)
        # random_move()
        # logout_login()
        send_keypress(i, 0x57)
        time.sleep(2)
        send_keypress(i, 0x53)
        time.sleep(2)
        send_keypress(i, 0x31)
        time.sleep(5)
        send_keypress(i, 0x32)
        time.sleep(5)
        send_keypress(i, 0x33)
        time.sleep(5)
        send_keypress(i, 0x34)
        time.sleep(5)
        send_keypress(i, 0x35)
        time.sleep(2)
        send_keypress(i, 0x36)
        time.sleep(5)
        
    time.sleep(100 + random.randint(100, 200))
