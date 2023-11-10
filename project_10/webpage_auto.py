import pyautogui
import time
import pyperclip  # It allows us to copy and paste the text in python file
from PIL import ImageGrab

pyautogui.moveTo(194, 950, 0.2)  # go to safari and open it
pyautogui.click()
time.sleep(0.5)
regions = ["seoul", "new york", "tokyo", "paris"]
for r in regions:
    pyautogui.hotkey("command", "t")  # create a new tab right after click the safari
    pyperclip.copy(f"{r} weather")
    pyautogui.hotkey("command", "v")  # paste the current region keyword
    time.sleep(0.5)
    pyautogui.write(["enter"])  # hit the enter to see the weather
    time.sleep(1)
    x1, y1, x2, y2 = (
        323,
        287,
        982,
        705,
    )  # x1, y1: left-top coordinate for screenshot // x2, y2: right-bottom coordinate for screenshot
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save(f"{r}.png")

# Following part is to check(with x and y coordinates) where my cursor is.
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)
