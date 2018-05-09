from flask import Flask

from time import sleep
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route("/")

def home():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# while True:
	# 	GPIO.output(4, GPIO.input(17))
	# 	sleep(.1)
	return str(GPIO.input(17))

app.run(host='0.0.0.0')
