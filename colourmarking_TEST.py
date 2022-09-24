from tkinter import *
import colorutils

def rgb_to_hex(percent):
    r,g,b=0,0,0
    if percent>=50:
        g=255
        r=b=2.5*(100-percent)
    else:
        r=255
        g=b=2.5*percent

    return colorutils.Color((r,g,b)).hex

while True:
    percent = int(input("Enter percentage: "))
    print(percent,rgb_to_hex(percent))



'''
print(colorutils.Color(hex="#19ff19").rgb)
print(colorutils.Color((255,100,100)).hex)
'''