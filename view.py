import pyautogui as pg
import time
import webbrowser

url = input("Enter Video url: ")

v = int(input("Enter views: "))


for i in range(v):
    webbrowser.open_new(url)

    time.sleep(10)

    pg.moveTo(1900, 10)
    pg.click()
