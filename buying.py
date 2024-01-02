
import time
import mss

from fishing import click, compute_icon_type, move


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
            
            move(inventory)
            click(inventory)
            time.sleep(5000)
            move(weaponTab)
            click(weaponTab)
            move(repairTab)
            click(repairTab)
            move(all_repair)
            click(all_repair)
            move(con)
            click(con)
            move(final_repair)
            click(final_repair)