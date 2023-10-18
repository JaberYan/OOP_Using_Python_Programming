import pyautogui
import time 
num_rows = int(input())
time.sleep(3)
for i in range(1,num_rows+1):
    for _ in range(i):
        pyautogui.write("#",interval=0.10)
    pyautogui.press('enter')