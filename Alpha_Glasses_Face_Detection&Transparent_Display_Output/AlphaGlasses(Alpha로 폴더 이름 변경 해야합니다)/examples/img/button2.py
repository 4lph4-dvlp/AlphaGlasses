#-*- coding: utf-8 -*-   
  
import RPi.GPIO as GPIO  
import time  
import os
import sys
def DetectButton(detect):
    GPIO.setmode( GPIO.BOARD )  
  
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
    while True:  
        input_state = GPIO.input(13)  
        myFile = open("test.txt","a")
        
        if input_state == False:  
            detect = 1 
            print("detect = 1")
            myFile.write(str(detect))
            myFile.close()
            return detect
            time.sleep(0.5) 
            
test = 0
DetectButton(test) 
os.system("python temp.py")
sys.exit()

