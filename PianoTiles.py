import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

pyautogui.click(1074,351,duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(981,291,(0,0,0)):
        click(981, 291)
    if pyautogui.pixelMatchesColor(1040,290,(0,0,0)):
        click(1040, 290)
    if pyautogui.pixelMatchesColor(1091,292,(0,0,0)):
        click(1091, 292)
    if pyautogui.pixelMatchesColor(1148,292,(0,0,0)):
        click(1148, 292)
