import subprocess
import time

try:
    import pyautogui
    from PIL import ImageGrab
    from functools import partial
except ModuleNotFoundError:
    subprocess.call(['versions/requirements.bat'])
    import pyautogui
    from PIL import ImageGrab
    from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

with open("config.txt", "r") as file:
    conf = float(file.readlines()[1].strip())

with open("config.txt", "r") as file:
    version = file.readlines()[4].strip()

inv_slot = 1

print("Program is running")
print(f"Version {version}")
print(f"confidence: {conf}")
while True:
    if pyautogui.locateOnScreen(f"versions\{version}.png", grayscale=True, confidence=conf) != None:
        pyautogui.click(button='right')
        print("Reeling Her In")

        if inv_slot == 9:
            inv_slot = 1
        else:
            inv_slot += 1

        pyautogui.press(f'{inv_slot}')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(6)
