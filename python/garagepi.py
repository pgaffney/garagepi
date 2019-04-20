import webiopi

GPIO = webiopi.GPIO

DOOR1 = 4
DOOR2 = 17

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the door to output
    GPIO.setFunction(DOOR1, GPIO.OUT)
    GPIO.setFunction(DOOR2, GPIO.OUT)
    return

# loop function is repeatedly called by WebIOPi
def loop():
    return

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(DOOR1, GPIO.HIGH)
    GPIO.digitalWrite(DOOR2, GPIO.HIGH)
    GPIO.cleanup()
    return
