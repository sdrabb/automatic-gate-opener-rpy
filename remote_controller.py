import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



def toggle_relay(number):
    GPIO.setup(number, GPIO.OUT)
    try:
        GPIO.output(3, GPIO.HIGH)
        print "OFF"

    except KeyboardInterrupt:
        print "exit"

        # Reset GPIO settings
        GPIO.cleanup()



