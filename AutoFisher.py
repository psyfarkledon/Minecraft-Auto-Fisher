try:
    import pyautogui
    import time
    from PIL import ImageGrab
    from functools import partial
except ModuleNotFoundError:
  print("[Missing Packages]: Please ensure you have installed everything in the requirements.txt file")
  input()


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

with open("config.txt", "r") as file:
    conf = float(file.readlines()[1].strip())

with open("config.txt", "r") as file:
    version = file.readlines()[4].strip()
    

print(version)
while True:
    if pyautogui.locateOnScreen(f"versions\{version}.png", grayscale=True, confidence=0.4) != None:
        pyautogui.click(button='right')
        print("Reeling Her In")
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(6)
