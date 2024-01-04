import subprocess
#from fishing import needcharge
from fishing import click,move
import mss
import numpy as np
import time


while True:
    with open('./needfix.txt','r') as file:
        content = file.read()

    if int(content) == 1:
        print("--------------------------start recharging-------------------------------")
        subprocess.run(["python", "./buying.py"])
        with open('./needfix.txt', 'w') as file:
            file.write('0')
        print("recharge finished'")

    else:
        print ("===============================starting fishing==================================")
        subprocess.run(["python", "./fishing.py"])


    time.sleep(1)
