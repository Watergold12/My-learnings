import time
import random
import sys

health = int(100)

def attackAlarm(alarm):
    print(alarm)

def attack():
    print("Skibidi, dop dop dop yes yes!")
    time.sleep(2)
    print("Skibidi dabudi DEEP DEEP!")
    time.sleep(2)

def death():
    global health
    health = int(0)
    print("You died!")
    time.sleep(1)
    sys.exit()


def mainCode():
    wait = random.uniform(0.5, 7.5)
    time.sleep(wait)
    attackAlarm("A skibidi toilet is attacking!")
    print("BRRR!!!")
    time.sleep(1)
    attack()
    attack()
    death()

mainCode()