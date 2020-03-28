# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:56:16 2019

@author: hosna
"""
import serial
import time

print("Start")

port="COM17" #This will be different for various devices and on windows it will probably be a COM port.

bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit

print("Connected")

bluetooth.flushInput() #This gives the bluetooth a little kick
#myArray = [1, 2, 3, 4, 5] 

for i in range(5): #send 5 groups of data to the bluetooth
    #bluetooth.write(str.encode("A"))
    #print("Ping")

    #time.sleep(0.1) #A pause between bursts
	#bluetooth.write(b"BOOP "+str.encode(str(i)))#These need to be bytes not unicode, plus a number

	input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
	print(input_data.decode())#These are bytes coming in so a decode is needed

bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob

print("Done")

