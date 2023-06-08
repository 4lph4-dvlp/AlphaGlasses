# -*- coding: utf-8 -*-
import time
#using library => github :  https://github.com/adafruit/Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
import os

import reading_txt as rt
import image as img
import button as bt

#Pin number(GPIO.BOARD 모드 기준의 핀번호)
RST = None     
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 현재 사용하고 있는 디스플레이 컨트롤러인 ssd1309와 호환가능한 ssd1306의 프리셋을 불러온다.
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Blink
draw.rectangle((0,0,width,height), outline=0, fill=0)

#y좌표 패딩값.(상하)
padding = -2
top = padding
bottom = height-padding
#x좌표 패딩값.(좌)
x = 0


font = ImageFont.load_default()
#"Bazzi.ttf"라는 글꼴 외에도 다른 ttc, ttf 파일을 추가하면 원하는 글꼴을 이용하여 출력하실 수 있습니다.(하단코드 Bazzi.ttf 부분 수정)
font_ko = ImageFont.truetype("/home/pi/Adafruit_Python_SSD1306/examples/Bazzi.ttf", 12, 0)
sw = 0

#list에서 가져온 텍스트를 이용하기 위해 save_text라는 리스트를 선언.
save_text = list()
rt.url_decode(save_text)

#로고 출력
filename = "/home/pi/Adafruit_Python_SSD1306/examples/Alpha.ppm"
img.print_image(filename)
#인공지능실행
#os.system('python3 /home/pi/Adafruit_Python_SSD1306/examples/first.py')

while True:

   
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    
    info = "Who?"
    if sw == 0:
        draw.text((x, top), "Info", font = font, fill = 255)
        draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
        print("0")
    elif sw == 1:
        draw.text((x, top), "Info", font = font, fill = 255)
        draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
        print("1")
    elif sw == 2:
        draw.text((x, top), "Info", font = font, fill = 255)
        draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
        print("2")
    elif sw == 3:
        draw.text((x, top), "Info", font = font, fill = 255)
        draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
        print("3")
    elif sw == 4:
        draw.text((x, top), "Info", font = font, fill = 255)
        draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
        print("4")
        disp.display()
        
        os.system('exit & python /home/pi/Adafruit_Python_SSD1306/examples/real.py')
        
       
   
    
    
    disp.image(image)
    disp.display()
    sw = sw + 1
    time.sleep(2)
    
