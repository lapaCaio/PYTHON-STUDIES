import pyautogui
from time import sleep

i = 0

while True:
    i = i + 1
    r = str(i)
    sleep(28)
    pyautogui.press('w')
    pyautogui.press('a')
    pyautogui.press('s')
    pyautogui.press('d')

    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('ciclos de automacao decorridos: ' + r)
    sleep(1)
    pyautogui.press('enter')
