from machine import Pin
import time

IV=Pin(2,Pin.OUT)
IM=Pin(4,Pin.OUT)
DV=Pin(5,Pin.OUT)
DM=Pin(15,Pin.OUT)

while True:
    IV.value(1)
    IM.value(1)
    time.sleep(5)
    IV.value(0)
    IM.value(0)
    time.sleep(0.1)

    DV.value(1)
    DM.value(1)
    time.sleep(3)
    DV.value(0)
    DM.value(0)
    time.sleep(0.1)# Write your code here :-)
