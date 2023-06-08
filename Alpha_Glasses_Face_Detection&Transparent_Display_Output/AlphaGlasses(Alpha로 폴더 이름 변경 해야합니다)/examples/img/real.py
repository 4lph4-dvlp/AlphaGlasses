# -*- coding: utf-8 -*-
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
import reading_txt as rt
import image as img
import button as bt
RST = None     

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0




# 현재 사용하고 있는 디스플레이 컨트롤러인 ssd1309와 호환가능한 ssd1306의 프리셋을 불러온다:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# 한글 폰트를 사용하기 위해 굴림ttc를 가져온다.(다른폰트도 파일만 있다면 사용가능!).
font = ImageFont.load_default()
font_ko = ImageFont.truetype("Bazzi.ttf", 12, 0)
sw = 0
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
save_text = list()
rt.url_decode(save_text)
#image = Image.open('Alpha.ppm').convert('1')
#time.sleep(2)
#disp.clear()
#disp.display()

filename = "Alpha.ppm"
img.print_image(filename)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    # Write two lines of text.
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
        sw = -1 
    #elif sw == 5:
        #draw.text((x, top), "Info", font = font, fill = 255)
        #draw.text((x+20, top+25), unicode(save_text[sw], 'utf-8', 'ignore'), font = font_ko, fill = 255)
       # sw = -1
    
    # Display image.
    disp.image(image)
    disp.display()
    sw = sw + 1
    time.sleep(2)
    
