import mss
import numpy as np
import time
import random
import pyautogui as pag

fishing = [1756, 853]
confirm = [888, 737]
Warning = {'left': 888, 'top': 737, 'width': 5, 'height': 5} #미끼채워
check = {'left': 1563, 'top': 759, 'width': 5, 'height': 5} #blinkimage
start_position = {'left': 1747, 'top': 853, 'width': 5, 'height': 5} #낚시대버튼
pag.PAUSE = 0.08
needfix = 0
expected_color = (0, 0, 0)  # Example: (0, 230, 250)
click_distance_x = 190  # Example: 20 pixels from x axis
click_distance_y = 120  # Example: 20 pixels from y axis
# 688>793 H
random_click_range = 10  # Example: 10 pixels
# 1550 > 1650 Width



def compute_icon_type(img):
    mean = np.mean(img, axis=(0, 1))
    r, g, b = mean[0], mean[1], mean[2]

    if r == 0 and g > 230 and b > 250:
        result = 'blink'
    elif r > 30 and g > 67 and b > 91 and r < 35 and g < 70 and b < 95:
        result = 'normal'
    elif r > 50 and g > 45 and b > 44 and r < 60 and g < 53 and b < 50:
        result = 'need start'
    elif r == 0 and g > 197 and b != 0 and r < 1 and g < 199 and b != 0 :
        result = 'yellow'
    elif r == 0 and g == 0 and b == 0 :
        result = 'black'
    else:
        result = 'unknown'

    return result
def click(coords):
    sleep_time = random.uniform(0,1)
    pag.moveTo(x=coords[0], y=coords[1], duration=0.0)
    time.sleep(sleep_time)
    print(sleep_time)
    pag.mouseDown()
    pag.mouseUp()


def find_color_on_screen(expected_color):
    screenshot = pag.screenshot()
    pixels = np.array(screenshot)
    matches = np.where(np.all(pixels == expected_color, axis=-1))
    if matches[0].size > 0:
        return matches[1][0], matches[0][0]
    return None, None



while True:
        with mss.mss() as sct:
            pop_img = np.array(sct.grab(check))[:, :, :3]
            need_start = np.array(sct.grab(start_position))[:, :, :3]
            waring = np.array(sct.grab(Warning))[:, :, :3]
            blink = compute_icon_type(pop_img)
            st = compute_icon_type(need_start)
            wn = compute_icon_type(waring)
        #If the specific color is found on the screen
            target_x, target_y = find_color_on_screen(expected_color)
            print("target :" , target_x,target_y)

        if st =='need start':
            click(fishing)
        elif st =='black' :
            click(fishing)
        #if blink == 'blink':
         #   print('tab!!!')
          #  click(fishing)

        if target_x is not None and target_y is not None:
                # Calculate random click position within the specified range
                random_x = random.randint(target_x - random_click_range, target_x + random_click_range)
                random_y = random.randint(target_y - random_click_range, target_y + random_click_range)

                # Calculate the click position within the specified distance from the detected color position
                click_x = min(max(random_x, target_x - click_distance_x), target_x + click_distance_x)
                click_y = min(max(random_y, target_y - click_distance_y), target_y + click_distance_y)
                here = (click_x,click_y)
                # Perform the click
                print(here)
                click(here)

        if wn == 'yellow':
            print("we have to recharge")
            click(confirm)
            with open('./needfix.txt' ,'w') as file:
                file.write('1')
            break






