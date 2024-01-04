
import time
import mss
import numpy as np
import pyautogui as pag
from fishing import click

bong = [397,933]
bong_tab=[397,789]
raw = [542,933]
raw_fish = [629,788]

click(bong)
time.sleep(1)
click(bong_tab)
time.sleep(1)            
click(raw)
time.sleep(1)            
click(raw_fish)
time.sleep(1)   