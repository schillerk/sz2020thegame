# from flask import Flask, render_template
# from flask_socketio import SocketIO

# from time import sleep
# # import RPi.GPIO as GPIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route("/")

# def home():
# 	return render_template('index.html')
# # 	GPIO.setmode(GPIO.BCM)
# # 	GPIO.setup(4, GPIO.OUT)
# # 	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# # 	# while True:
# # 	# 	GPIO.output(4, GPIO.input(17))
# # 	# 	sleep(.1)
# # 	return str(GPIO.input(17))

# if __name__ == '__main__':
#     socketio.run(app)
# 	# app.run(host='0.0.0.0')

from flask import *
from flask_socketio import SocketIO
# import RPi.GPIO as GPIO
import time
import json

app = Flask(__name__)
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

start = time.time()
hall = 17

GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(hall, GPIO.IN, pull_up_down = GPIO.PUD_UP)

@app.route("/")
def index():
        return render_template('speedo.html')

@app.route('/thing')
def thing():
        def read_thing_state():
            while True:
                thing_state = { 'start' : get_start() }
                yield 'data:{0}\n\n'.format(json.dumps(thing_state))
        return Response(read_thing_state(), mimetype='text/event-stream')

def get_start():
    return start

def get_pulse():
    start = time.time()

if __name__ == '__main__':
    GPIO.add_event_detect(hall, GPIO.FALLING, callback=get_pulse, bouncetime=20)
    socketio.run(app, host='0.0.0.0', port=9000, debug=True)