from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# Tile 1 position X:  373 Y:  730
# Tile 2 position X:  448 Y:  730
# Tile 3 position X:  550 Y:  730
# Tile 4 position X:  641 Y:  730
X = [373, 448, 550, 641]
Y = 730


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def check_pixel_color(x, y, r, g, b):
    pixel_r, pixel_g, pixel_b = pyautogui.pixel(x, y)
    return pixel_r == r and pixel_g == g and pixel_b == b


playing = False

# e for exit
while keyboard.is_pressed('e') == False:

    # s for start
    if keyboard.is_pressed('s') == True:
        playing = True
    # p for pause
    if keyboard.is_pressed('p') == True:
        playing = False

    if playing == False:
        continue

    for i in range(4):
        if check_pixel_color(X[i], Y, 0, 0, 0):
            click(X[i], Y)
