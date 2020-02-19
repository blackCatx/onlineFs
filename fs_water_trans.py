import pyautogui
import time
from datetime import datetime
import random

#
nums = [0, 0, 10, 10]


def action(count):
    pyautogui.keyDown('w')
    time.sleep(0.3)
    pyautogui.keyUp('w')
    time.sleep(5)
    time.sleep(random.randint(1, 3))
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')
    time.sleep(random.randint(1, 3))
    # Buff
    if random.random() < 0.5:
        pyautogui.press("1")
        time.sleep(5)
    if random.random() < 0.5:
        pyautogui.press("2")
        time.sleep(5)
    if random.random() < 0.5:
        pyautogui.press("3")
        time.sleep(5)
    if random.random() < 0.5:
        pyautogui.press("4")
        time.sleep(5)

    if random.random() < 0.5:
        # dat
        if nums[0] > 0:
            pyautogui.press("5")
            nums[0] -= 1
        else:
            pyautogui.press("1")
            nums[0] += nums[2]
        time.sleep(15)
        pyautogui.press('space')
        time.sleep(2)
    if random.random() < 0.5:
        # drink
        if nums[1] > 0:
            pyautogui.press("6")
            nums[1] -= 1
        else:
            pyautogui.press("2")
            nums[1] += nums[3]
        time.sleep(15)
        pyautogui.press('space')
        time.sleep(2)

    #back
    # pyautogui.mouseDown(button='right')
    # pyautogui.move(-50, 0, duration=0.75)
    # pyautogui.mouseUp(button='right')
    # pyautogui.mouseDown(button='right')
    # pyautogui.move(-50, 0, duration=0.75)
    # pyautogui.mouseUp(button='right')


time.sleep(5)
st = datetime.now()
count = 0
while True:
    action(count)
    count += 1
    time.sleep(random.randint(60, 90))
