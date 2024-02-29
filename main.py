import subprocess
import numpy as np
import time


while True:
    with open('./needfix.txt','r') as file:
        content = file.read()

    if int(content) == 1:
        print("--------------------------start recharging-------------------------------")
        subprocess.run(["python3", "./buying.py"])
        with open('./needfix.txt', 'w') as file:
            file.write('0')
        print("recharge finished'")

    else:
        print ("===============================starting fishing==================================")
        subprocess.run(["python3", "./fishing.py"])


    time.sleep(1)
