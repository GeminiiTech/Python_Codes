import pyautogui
import time

#wait for the user to open a form or window to fill out
time.sleep(10)


#Type in the text and press Enter
pyautogui.typewrite("0617")
pyautogui.press("enter")

#Move the mouse and click a button
pyautogui.moveTo(100,100)
pyautogui.click()