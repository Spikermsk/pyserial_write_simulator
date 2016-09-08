#!/usr/bin/python
import serial
import time
import random
import os

print "Startingup..."

#sdev = open("/dev/ttyUSB0", "r")
serial_dev = os.getenv("HOST_DEV1")
if serial_dev is None:
    print "Location of serial device file is not provided in the env context.."
    serial_dev="/dev/tty.usbserial"
print "Serial Dev: " + serial_dev
sdev = serial.Serial(port=serial_dev, baudrate=9600) 
sdev.bytesize = serial.EIGHTBITS #number of bits per bytes

sdev.parity = serial.PARITY_NONE #set parity check: no parity

sdev.stopbits = serial.STOPBITS_ONE #number of stop bits
sdev.timeout = 5
print "Serial:  %s\n" % sdev
while True:
    # send the character to the device
    # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
    temp = random.uniform(20.0,50.0)
    temp=round(temp, 2)
    humidity=random.randint(30,100)
    humidity=round(humidity,2)
    pressure=random.uniform(14.0, 20.0) 	
    pressure=round(pressure,2)
    out = ''
    out=str(temp) + "," + str(humidity) + "," + str(pressure) 	
    print "Writing: %s\n" % out
    sdev.write(out + '\r\n')
    # let's wait 3 second before reading output (let's give device time to answer)
    time.sleep(5)

sdev.close()
