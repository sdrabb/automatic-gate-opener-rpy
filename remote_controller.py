import RPi.GPIO as GPIO
import time




def toggle_relay(number):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(number, GPIO.OUT)
    try:
        GPIO.output(number, GPIO.LOW)
	time.sleep(1)
	GPIO.output(number, GPIO.HIGH)	
        print "OFF"

    except KeyboardInterrupt:
        print "exit"

        # Reset GPIO settings
        GPIO.cleanup()



