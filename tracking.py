import pyautogui as pag


while True:
    x, y = pag.position()
    position_str = 'X: '+ str(x) + ' Y: ' + str(y)
    print(position_str)