import pyautogui
import time
while True:
    if pyautogui.locateOnScreen("image.png", grayscale=True, confidence=0.5) != None:
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(6)



