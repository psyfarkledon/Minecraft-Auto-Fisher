<<<<<<< HEAD
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
=======
try:
    import pyautogui
    import time
    from PIL import ImageGrab
    from functools import partial
except ModuleNotFoundError:
  print("[Missing Packages]: Please ensure you have installed everything in the requirements.txt file")
  input()
>>>>>>> 63d989fd83596901b3e16393829cdf3ff39736f9


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

with open("config.txt", "r") as file:
    conf = float(file.readlines()[1].strip())

with open("config.txt", "r") as file:
    version = file.readlines()[4].strip()
    

print("Program is running")
print(f"Version {version}")
print(f"confidence: {conf}")
while True:
    if pyautogui.locateOnScreen(f"versions\{version}.png", grayscale=True, confidence=conf) != None:
        pyautogui.click(button='right')
        print("Reeling Her In")
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(6)
