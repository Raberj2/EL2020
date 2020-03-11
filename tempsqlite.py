#Import Libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import sqlite3 as sql
import os
import smtplib

tempSensor = Adafruit_DHT.DHT11
#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #red light
GPIO.setup(13, GPIO.OUT) #green light
#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #touch
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #hum
#This function will make the light blink once

con = sql.connect('log/tempLog.db')
cur = con.cursor()

def readF(pin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, 12)
	temperature = temperature*9/5.0+32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}'.format(temperature)
		print(tempFahr)
	else:
		print('Error Reading Sensor')
	return tempFahr

def readH(pin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, 12)
	if humidity is not None and temperature is not None:
		humid = '{0:0.1f}'.format(humidity)
		print(humid)
	else:
		print('Error Reading Sensor')
	return humid


def lightrange(temp):
	if temp >= 70 and temp <= 80:
		GPIO.output(17,True)
		GPIO.output(13,False)
	else:
		GPIO.output(17, False)
		GPIO.output(13, True)
	return

#unable to finish due to reasons explained in readme


#def blinkOnce(pin):
#	GPIO.output(pin,True)
#	time.sleep(0.1)
#	GPIO.output(pin,False)
#	time.sleep(0.1)

#touchstatus = False
#def read_touchsensor():
#	global touchstatus
#	if (GPIO.input(13)==True):
#		touchstatus = not touchstatus
#		if touchstatus:
#			blinkOnce(17)
#			data = readF(12)
#		else:
#			GPIO.output(17,False)
#	pass

#Call the blinkOnce function above in a loop
#for i in range(10):
#	blinkOnce(17)
#cleanup the GPIO when done
try:
		while True:
#			read_touchsensor()
#			time.sleep(60)
			dataT = readF(12)
			dataH = readH(12)
			lightrange(dataT)
			cur.execute('INSERT INTO tempLog values(?,?,?)',(time.strftime('%Y-%m-%d %H:%M:%S'), dataT, dataH))
			con.commit()
			table = con.execute("select * from tempLog")
			time.sleep(60)
			os.system('clear')
#			log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(dataT) + ", " + str(dataH)))
#			log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(dataH)))

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	exit(0)
	GPIO.cleanup()
