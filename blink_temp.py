#Import Libraries
import RPi.GPIO as GPIO
import time

#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
#This function will make the light blink once
def blinkOnce(pin):
	
	GPIO.output(pin,True)
	time.sleep(0.1)
	GPIO.output(pin,False)
	time.sleep(0.1)

touchstatus = False
def read_touchsensor():
	global touchstatus
	if (GPIO.input(13)==True):
		touchstatus = not touchstatus
		if touchstatus:
			blinkOnce(17)
		else:
			GPIO.output(17,False)
	pass

#Call the blinkOnce function above in a loop
#for i in range(10):
#	blinkOnce(17)
#cleanup the GPIO when done
def main():
	while True:
		read_touchsensor()

if __name__ == '__main__':
	try:
		main()
		pass
	except KeyboardInterrupt:
		pass
GPIO.cleanup()
