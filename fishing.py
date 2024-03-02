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
expected_color = (248, 239, 80)  # 낚시버튼(86,172,152)
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
    screenshot_rgb = screenshot.convert("RGB")
    pixels = np.array(screenshot_rgb)
    matches = np.where(np.all(pixels == expected_color, axis=-1))
    if matches[0].size > 0:
        return matches[1][0], matches[0][0]
    else:
        print("couldnt find color")
    return 0,0



while True:
    try:
        with mss.mss() as sct:
#           pop_img = np.array(sct.grab(check))[:, :, :3]
#           need_start = np.array(sct.grab(start_position))[:, :, :3]
#           waring = np.array(sct.grab(Warning))[:, :, :3]
#           blink = compute_icon_type(pop_img)
#           st = compute_icon_type(need_start)
#           wn = compute_icon_type(waring)
        #If the specific color is found on the screen
            target_x, target_y = find_color_on_screen(expected_color)
            print( "target :" , target_x,target_y )

#       if st =='need strt':
#           click(fishing)
#       elif st =='black' :
#           click(fishing)
#       if blink == 'blink':

          #  print('tab!!!')
             #click(fishing)
            # Calculate the click position within the specified distance from the detected color position
            here = (target_x+80,target_y+60)
            # Perform the click
            print("target: ",target_x,target_y)
            print("real tap ",here)
            #if target_x != 0 and target_y != 0:
                #click(here)

#       if wn == 'yellow':
#           print("we have to recharge")
#           click(confirm)
#           with open('./needfix.txt' ,'w') as file:
#               file.write('1')
            break
    except pag.ImageNotFoundException:
        print("이미지를 찾지 못했습니다. 다시 시도합니다.")
        time.sleep(1)





