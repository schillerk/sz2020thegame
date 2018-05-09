import time
import RPi.GPIO as GPIO

lp = 4
bp = 17

print "hey"

GPIO.setmode(GPIO.BCM)
GPIO.setup(lp, GPIO.OUT)
GPIO.setup(bp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
	GPIO.output(bp, True)
