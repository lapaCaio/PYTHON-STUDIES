import _thread
import time
import pyautogui


def click_thread():
    while True:
        if pyautogui.mouseDown(button='left'):
            pyautogui.click()
            time.sleep(0.1)
        else:
            break


def exit_thread():
    while True:
        if 'p' in pyautogui.typewrite('', interval=0.1):
            print("Programa encerrado.")
            _thread.interrupt_main()
            break


_thread.start_new_thread(exit_thread, ())
while True:
    _thread.start_new_thread(click_thread, ())
