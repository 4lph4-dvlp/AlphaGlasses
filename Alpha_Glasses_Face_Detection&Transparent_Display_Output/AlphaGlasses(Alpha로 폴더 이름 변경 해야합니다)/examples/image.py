#-*- coding:utf-8 -*-
import time, Adafruit_GPIO.SPI as SPI, Adafruit_SSD1306
from PIL import Image
#Pin number(GPIO.Board)
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
#객체정의
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
#이미지 출력 함수
def print_image(Filename):
    image = Image.open(Filename).convert('1')
    disp.image(image)
    disp.display()
    time.sleep(2)
    disp.clear()
    disp.display()