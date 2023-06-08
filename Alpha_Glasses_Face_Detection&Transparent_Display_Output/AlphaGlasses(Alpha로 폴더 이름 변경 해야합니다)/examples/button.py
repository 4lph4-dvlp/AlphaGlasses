#-*- coding: utf-8 -*-   
  
import RPi.GPIO as GPIO  
import time  


def DetectButton(detect):
    GPIO.setmode( GPIO.BCM )  
  
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
    while True:  
        input_state = GPIO.input(18)  
        myFile = open("test.txt","a")
        
        if input_state == False:  
            detect = 1 
            print("detect = 1")
            myFile.write(str(detect))
            myFile.close()
            return detect
            time.sleep(0.5) 
            detect = 0
            print("detect = 0")
test = 0
DetectButton(test)