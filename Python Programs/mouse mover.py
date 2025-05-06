import pyautogui as pag
import time

while True:
    pag.moveTo(150, 150, duration=1)
    pag.moveTo(300, 100, duration=1)
    pag.moveTo(400, 400, duration=1)
    pag.moveTo(700, 300, duration=1)
    pag.moveTo(600, 400, duration=1)
    time.sleep(5)  # Wait for 5 seconds
