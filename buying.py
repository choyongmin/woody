
import time
import mss
import numpy as np
from fishing import click, compute_icon_type


inventory = [1188,859]
pink = {'left': 1178 , 'top': 861, 'width': 2, 'height': 2}
weaponTab = [400,351]
repairTab = [1461,774]
all_repair = [722,900]
con = [1100,630]
final_repair =[1504,904]


while True:

    with mss.mss() as sct:
        inv = np.array(sct.grab(pink))[:, :, :3]
        inv_pink = compute_icon_type(inv)
        print("hi")
        if inv_pink == 'pink':

            click(inventory)
            time.sleep(5000)
            click(weaponTab)
            click(repairTab)
            click(all_repair)
            click(con)
            click(final_repair)
