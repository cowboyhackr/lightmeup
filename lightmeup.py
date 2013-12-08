import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime

PIR = 23
LED = 24
TAIL = 25

pirVal = False	# we start, assuming no motion detected
startTime = datetime.now() #initialize
maxSeconds = 10
duration = datetime.now() - datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TAIL, GPIO.OUT)


while True:
    pirVal = GPIO.input(PIR)	# read input value

    sys.stdout.write(str(pirVal) + '\n')

    if (pirVal == True):
	duration = datetime.now() - datetime.now()
 
    durationSeconds = int(duration.total_seconds())
    if (dimport RPi.GPIO as GPIO
import time
import sys
from datetime import datetime

PIR = 23
LED = 24
TAIL = 25

pirVal = False	# we start, assuming no motion detected
startTime = datetime.now() #initialize
maxSeconds = 10
duration = datetime.now() - datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TAIL, GPIO.OUT)


while True:
    pirVal = GPIO.input(PIR)	# read input value

    sys.stdout.write(str(pirVal) + '\n')

    if (pirVal == True):
	duration = datetime.now() - datetime.now()
 
    durationSeconds = int(duration.total_seconds())
    if (durationSeconds < maxSeconds):	# check if the input is HIGH
        GPIO.output(LED,True)	# turn LED ON
	GPIO.output(TAIL,True)	# turn TAIL ON
        duration = datetime.now() - startTime
        sys.stdout.write(str(durationSeconds) + '\n')
        sys.stdout.write('duration\n')
	
   
    else:
        GPIO.output(LED, False)	# turn LED OFF
	GPIO.output(TAIL,False)	# turn TAIL OFF
	#reset
	startTime = datetime.now()
        #duration = datetime.now() - datetime.now()
	sys.stdout.write('IN ELSE:  ' + str(duration.total_seconds()) + '\n')


urationSeconds < maxSeconds):	# check if the input is HIGH
        GPIO.output(LED,True)	# turn LED ON
	GPIO.output(TAIL,True)	# turn TAIL ON
        duration = datetime.now() - startTime
        sys.stdout.write(str(durationSeconds) + '\n')
        sys.stdout.write('duration\n')
	
   
    else:
        GPIO.output(LED, False)	# turn LED OFF
	GPIO.output(TAIL,False)	# turn TAIL OFF
	#reset
	startTime = datetime.now()
        #duration = datetime.now() - datetime.now()
	sys.stdout.write('IN ELSE:  ' + str(duration.total_seconds()) + '\n')
