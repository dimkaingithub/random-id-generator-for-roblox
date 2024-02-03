import keyboard as keyb
import random as rand
from time import sleep
import mouse
while True:
    keyb.wait("r")
    mouse.click("left")
    sleep(0.1) 
    mouse.click("left")
    sleep(0.1)
    id = str(rand.randint(10000000, 99999999))
    keyb.write(id)
    sleep(0.2)
    keyb.press("enter")
    sleep(0.1)
    keyb.release("enter")
    print(id)