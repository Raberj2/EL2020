#Import Libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

tempSensor = Adafruit_DHT.DHT11

#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #touch
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #hum
#This function will make the light blink once
def readF(pin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, 12)
	temperature = temperature*9/5.0+32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
		print(tempFahr)
	else:
		print('Error Reading Sensor')
	return tempFahr
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
			data = readF(12)
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
			time.sleep(.2)
			data = readF(12)
			log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(data)))

if __name__ == '__main__':
	try:
		with open("log/templog.csv", "a") as log:
			main()
			pass
	except KeyboardInterrupt:
		pass
GPIO.cleanup()
