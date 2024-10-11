from tkinter import messagebox
import pyautogui
from time import sleep


#
# DO NOT CHANGE ANY OF THE REMAINING PROGRAM
# CURRENT LOOP TIME = 148 SECONDS
# LOOP MUST EXCEED 120 SECONDS DUE TO TEK POD COOLDOWN

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

SELF_KILL_POS = Point(0, 0)
SELF_SEARCH_BED_POS = Point(0, 0)
SELF_SELECT_BED_POS = Point(0, 0)
SELF_SPAWN_BED_POS = Point(0, 0)

print("Checking Resolution Configuration")

screenSize = pyautogui.size()
if screenSize.width == 2560 and screenSize.height == 1440:
    SELF_KILL_POS = Point(295,370)
    SELF_SEARCH_BED_POS = Point(295,1291)
    SELF_SELECT_BED_POS = Point(489,291)
    SELF_SPAWN_BED_POS = Point(2171,1283)
elif screenSize.width == 1920 and screenSize.height == 1080:
    SELF_KILL_POS = Point(220,278)
    SELF_SEARCH_BED_POS = Point(208,969)
    SELF_SELECT_BED_POS = Point(260,220)
    SELF_SPAWN_BED_POS = Point(1625,961)
else:
    messagebox.showinfo("Single Mother", f"Your resolution of {screenSize.width}x{screenSize.height} does not receive child support.")
    exit(1)

print("Entering Main Loop")
sleep(5)

while True:
    print("Giganto bot running")

    pyautogui.press('capslock')
    sleep(1)
    pyautogui.leftClick(SELF_KILL_POS.x, SELF_KILL_POS.y)
    sleep(6)
    pyautogui.press("e")
    sleep(20)
    pyautogui.leftClick(SELF_SEARCH_BED_POS.x, SELF_SEARCH_BED_POS.y)
    sleep(1)
    pyautogui.typewrite("giganto bed", interval=0.05)
    sleep(1)
    pyautogui.leftClick(SELF_SELECT_BED_POS.x, SELF_SELECT_BED_POS.y)
    sleep(1)
    pyautogui.leftClick(SELF_SPAWN_BED_POS.x, SELF_SPAWN_BED_POS.y)
    sleep(25)
    pyautogui.press("e")
    sleep(12)
    pyautogui.press("e")
    sleep(3)
    pyautogui.press("e")
    sleep(12)
    pyautogui.press("e")
    sleep(3)
    pyautogui.press("e")
    sleep(12)
    pyautogui.press("e")
    sleep(3)
    pyautogui.press("e")
    sleep(12)
    pyautogui.press("e")
    sleep(3)
    pyautogui.press("e")
    sleep(12)
    pyautogui.press("e")
    sleep(3)
    pyautogui.press("e")
    sleep(12)
    
    
    

 
