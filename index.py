import keyboard
import time

def interact():
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')
    time.sleep(1)
    return

def leavePCToSpot():
    keyboard.press('s')
    time.sleep(2)
    keyboard.release('s')
    keyboard.press('d')
    time.sleep(3)
    keyboard.release('d')
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')
    keyboard.press('d')
    time.sleep(2.75)
    keyboard.release('d')
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')
    return

def battle():
    keyboard.press('9')
    time.sleep(1)
    keyboard.release('9')
    time.sleep(10)
    keyboard.press('z')
    time.sleep(1)
    keyboard.release('z')
    keyboard.press('z')
    time.sleep(1)
    keyboard.release('z')
    keyboard.press('z')
    time.sleep(1)
    keyboard.release('z')
    keyboard.press('z')
    time.sleep(1)
    keyboard.release('z')
    time.sleep(10)
    return

def leaveSpotToPC():
    keyboard.press('a')
    time.sleep(4)
    keyboard.release('a')
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')
    keyboard.press('a')
    time.sleep(2.3)
    keyboard.release('a')
    keyboard.press('w')
    time.sleep(3)
    keyboard.release('w')
    return

""" 
    It's meant to be used with your trainer's in running mode
    and inside battle frontier in hoenn poke center, right where
    you can press Z to heal your pokemons.
"""
def init():
    leavePCToSpot()
    interact()
    battle()
    time.sleep(1)
    battle()
    time.sleep(1)
    battle()
    time.sleep(1)
    battle()
    time.sleep(1)
    leaveSpotToPC()
    time.sleep(2)
    interact()
    time.sleep(3)
    return

keyboard.add_hotkey('shift+space', init)
keyboard.wait('esc')
