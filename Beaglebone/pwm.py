import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
import socket
import sys
from time import sleep

myPWM="P8_13"
fsr = "P9_39"

ADC.setup()
PWM.start(myPWM, 0, 100)

serverAddr = ('192.168.7.1', 7000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(serverAddr)

def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

prev=0
prevdf=0
count=0

while True:
        reading = None
	reading = ADC.read(fsr)*100
        reading = int(round(reading))
	client.send(str(reading)+'\0')
	print('fsr value: %i' % (reading))
	if reading > 2:
		if reading > prev or (prev>=reading and (prev-reading)<2):
			if reading>prev:
				df=reading-prev
				prevdf=df
			else:
				 df=prevdf
			FC = map(df, 3, 60, 90, 130)
			PWM.set_frequency(myPWM, FC) 
                	DC = map(df, 3, 60, 30, 50)
                	PWM.set_duty_cycle(myPWM, DC)
			count=count+1
		if  reading<=prev or (prev<=reading and (reading-prev)<2): 
			PWM.set_duty_cycle(myPWM, 0)
        if reading <= 2:
                PWM.set_duty_cycle(myPWM, 0)
	prev = reading

client.close()
