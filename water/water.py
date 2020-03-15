# coding=utf-8
import pyautogui
import time
import random
import win32gui

# 做水和面包数量
nums = [0, 0, 10, 6]
count = 0

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

def send_msg_clickkey(hwnd, key):
    win32gui.SendMessage(hwnd, 0x100, key, 0)
    win32gui.SendMessage(hwnd, 0x101, key, 0)

def send_msg_move_up(hwnd):
    win32gui.SendMessage(hwnd, 0x100, 38, 0)
    time.sleep(0.3)
    win32gui.SendMessage(hwnd, 0x101, 38, 0)


def send_msg_move_down(hwnd):
    win32gui.SendMessage(hwnd, 0x100, 40, 0)
    time.sleep(0.5)
    win32gui.SendMessage(hwnd, 0x101, 40, 0)

def send_msg_jump(hwnd):
    win32gui.SendMessage(hwnd, 0x100, 0x20, 0)
    win32gui.SendMessage(hwnd, 0x101, 0x20, 0)
    time.sleep(1) 

def logout_login():
    pyautogui.press('esc')
    time.sleep(5)
    pyautogui.click(960, 618)
    time.sleep(30)
    pyautogui.click(960, 988)
    time.sleep(30)


moves = [('w',), ('a',), ('s',), ('d',),
         ('w', 'a'), ('w', 'd'), ('s', 'a'), ('s', 'd')]


def random_move():
    for i in range(random.randint(5, 8)):
        pyautogui.hotkey(*random.choice(moves),
                         interval=(0.2 + random.random() * 0.5))

def transform(i):
    print("transform <<<<")

    time.sleep(random.randint(5, 6))

def action(i):



    # # water 
    # send_msg_clickkey(i, 49)
    # time.sleep(random.randint(3, 4))
    # send_msg_clickkey(i, 50)
    # time.sleep(random.randint(3, 4))
    # # buff
    # send_msg_clickkey(i, 51)
    # time.sleep(random.randint(2, 3))
    # send_msg_clickkey(i, 52)
    # time.sleep(random.randint(2, 3))
    # drink
    # send_msg_clickkey(i, 53)
    # time.sleep(1)
    # send_msg_clickkey(i, 54)
    # time.sleep(random.randint(3, 5))

    # if random.random() < 0.5:
    #     pyautogui.press(3)
    #     time.sleep(5)
    send_msg_move_down(i)

    time.sleep(random.randint(3, 4))
  
    if random.random() < 0.5:
        # water 
        send_msg_clickkey(i, 49)#1
        time.sleep(random.randint(3, 4))
        send_msg_clickkey(i, 50)#2
        time.sleep(random.randint(3, 4))
        nums[0] += nums[2]
        nums[1] += nums[3]
        time.sleep(1)


  # 上Buff
    if random.random() < 0.5:
        # buff
        send_msg_clickkey(i, 51)#3
        time.sleep(random.randint(2, 3))
        send_msg_clickkey(i, 52)#4
        time.sleep(random.randint(2, 3))
        time.sleep(2)

    if random.random() < 0.5:
        # 做面包吃面包
        # 做水喝水
        if nums[0] > 0:
            send_msg_clickkey(i, 54)#6
            nums[0] -= 1
            send_msg_clickkey(i, 53)#5
            nums[1] -= 1
            time.sleep(random.randint(3, 5))
            send_msg_jump(i)
        else:
            send_msg_clickkey(i, 50)#2
            time.sleep(random.randint(3, 4))
            nums[0] += nums[2]
            send_msg_clickkey(i, 49)#1
            time.sleep(random.randint(3, 4))
            nums[1] += nums[3]
        time.sleep(2)

    if random.random() < 0.5:
        # 做水喝水
        if nums[1] > 0:
            send_msg_clickkey(i, 53)#5
            nums[1] -= 1
            time.sleep(random.randint(3, 5))
            send_msg_jump(i)
        else:
            send_msg_clickkey(i, 49)#1
            time.sleep(random.randint(3, 4))
            nums[1] += nums[3]
        time.sleep(2)

    send_msg_move_up(i)

# time.sleep(10)
while True:
    print("begin")
    for i in wow_windows:
        action(i)
        # logout_login()
        if count != 0 and count % 5 == 0:
            transform(i)
    time.sleep(240 + random.randint(1, 9))
    count += 1  #35s

