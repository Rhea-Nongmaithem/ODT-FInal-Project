#import libraries
from machine import Pin 
import time

#assigning GPIO Pins to the valves and pumps
IV=Pin(2,Pin.OUT)
IM=Pin(4,Pin.OUT)
DV=Pin(5,Pin.OUT)
DM=Pin(15,Pin.OUT)

while True: #Loop to always run
    #Turn on inflation
    IV.value(1) 
    IM.value(1)
    time.sleep(5) #inflate for 5 seconds

    #Turn off inflation
    IV.value(0)
    IM.value(0)
    time.sleep(0.1) #small time interval between inflation and deflation

    #Turn on deflation
    DV.value(1)
    DM.value(1)
    time.sleep(3) #deflate for 3 seconds

    #Turn off deflation
    DV.value(0)
    DM.value(0)
    time.sleep(0.1) #small time interval between deflation and inflation
