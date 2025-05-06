import pyautogui as pag
import time

pag.FAILSAFE = False

while True:
    pag.moveTo(1000, 500, duration=3)
    pag.moveTo(500, 800, duration=3)
    pag.moveTo(700, 200, duration=3)
    pag.moveTo(1700, 350, duration=3)
    pag.moveTo(1500, 400, duration=3)
    pag.moveTo(1450, 650, duration=3)
    time.sleep(10)