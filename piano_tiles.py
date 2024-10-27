import pyautogui as gui
import keyboard 
from time import sleep 
import win32api
import win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)  
    sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

gui.click(1192,614, duration=2)
while keyboard.is_pressed('1') == False:
    if gui.pixelMatchesColor(723,390, (0,0,0)):
        click(723,390)
    if gui.pixelMatchesColor(875,390, (0,0,0)):
        click(875,390)
    if gui.pixelMatchesColor(1030,390, (0,0,0)):
        click(1030,390)
    if gui.pixelMatchesColor(1188,390, (0,0,0)):
        click(1188,390)
    