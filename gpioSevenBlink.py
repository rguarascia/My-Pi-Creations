## Ryan Guarasica
## June, 11, 2014
## My first LED simulation with the Raspberry Pi and a BeardBoard.
## I also have a self-powered fan on P2.

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Contains 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

##Does the blinking
def Blink(numTimes,speed):
    for x in range(0,numTimes):
        print "Looped: " + str(x+1)
        time.sleep(speed)
        GPIO.output(7,True)
        GPIO.output(11,False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        time.sleep(speed)
        GPIO.output(7,False)
        GPIO.output(11, True)
        time.sleep(speed)
        GPIO.output(11, False)
        GPIO.output(13, True)
        time.sleep(speed)
        GPIO.output(13, False)
        GPIO.output(15, True)
    for y in range(0,5):
        print "Blink" 
        time.sleep(0.2)
        GPIO.output(7,True)
        GPIO.output(11,True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        time.sleep(0.2)
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13, False)
        GPIO.output(15, False)
    print "Done"  
    GPIO.cleanup() ##Shuts the ports off

## Weird glitch where 11, 15 are on so a quick fix
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13, False)
GPIO.output(15, False)
times = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

##Float allows milliseconds
Blink(int(times),float(speed))
