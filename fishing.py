import pyautogui as pag
import mss
import cv2
import numpy as np
import time
import random


fishing = [1715, 827]
confirm = [1041, 689]
Warning = {'left': 1041, 'top': 689, 'width': 5, 'height': 5}
check = {'left': 1610, 'top': 750, 'width': 5, 'height': 5}
start_position = {'left': 1710, 'top': 800, 'width': 5, 'height': 5}
pag.PAUSE = 0.08
# 688>793 H
# 1550 > 1650 Width


def compute_icon_type(img):
    mean = np.mean(img, axis=(0, 1))
    r, g, b = mean[0], mean[1], mean[2]

    if r == 0 and g > 230 and b > 250:
        result = 'blink'
    elif r > 30 and g > 67 and b > 91 and r < 35 and g < 70 and b < 95:
        result = 'normal'
    elif r > 150 and g > 165 and b > 170 and r < 155 and g < 170 and b < 180:
        result = 'need start'
    elif r == 0 and g > 197 and b != 0 and r < 1 and g < 199 and b != 0 :
        result = 'yellow'
    elif r > 159 and g > 78 and b > 30 and r < 170 and g < 90 and b < 40 :
        result = 'pink'
    else:
        result = 'unknown'

    return result


def click(coords):
    pag.moveTo(x=coords[0], y=coords[1], duration=0.0)
    time.sleep(1)
    pag.mouseDown()
    pag.mouseUp()


while True:
    with mss.mss() as sct:
        pop_img = np.array(sct.grab(check))[:, :, :3]
        need_start = np.array(sct.grab(start_position))[:, :, :3]
        waring = np.array(sct.grab(Warning))[:, :, :3]
        blink = compute_icon_type(pop_img)
        st = compute_icon_type(need_start)
        wn = compute_icon_type(waring)
        print(st)
        #print(blink)
        #print(wn)



        if st =='need start':
            click(fishing)

        if blink == 'blink':
            print('tab!!!')
            sleep_time = random.randint(0,3)
            click(fishing)

        if wn == 'yellow':
            print("we have to recharge")
            click(confirm)
            needcharge = 1
            break





