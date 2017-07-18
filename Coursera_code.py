# define LED digital pin
# define push button as digital pin
# while button = False
    # led True
    #delay
    #led False

# if button  = True
    #led True

import RPi.GPIO as GPIO
import time

ledpin = 2
butpin = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)  #Connecting LED to output pin 1
GPIO.setup(butpin, GPIO.IN, pull_up_down = GPIO.PUD_UP)   #Connecting Push button to input pin 2


while True:
    value = GPIO.input(butpin) # read input value from push button
    print(value)
    if value is 1: 
        
        GPIO.output(ledpin, True)
        time.sleep(0.5)
        GPIO.output(ledpin, False)

    else: # value is 0
        GPIO.output(ledpin, True) 
    

