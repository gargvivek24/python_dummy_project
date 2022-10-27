import pyautogui as pg
import time
time.sleep(5)

for i in range(10):
    pg.write('hello')
    time.sleep(2)
    pg.press('Enter')


# for i in range (10):
#     if i==0:
#         continue
#     if i%2==0:
#         print(i)


