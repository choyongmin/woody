import subprocess
#from fishing import needcharge
from fishing import click,move
import mss
import numpy as np
import time


buyingpy = 'C:/Users/whdyd/OneDrive/바탕 화면/일/woody/buying.py'
Xpoint = [1812, 135]
needfix = 0
while True:
    if needfix == 1:
        print("--------------------------start recharging-------------------------------")
        subprocess.run(["python", "./buying.py"])
        needfix = 0

    else:
        print ("===============================starting fishing==================================")
        subprocess.run(["python", "./fishing.py"])


    time.sleep(1)
