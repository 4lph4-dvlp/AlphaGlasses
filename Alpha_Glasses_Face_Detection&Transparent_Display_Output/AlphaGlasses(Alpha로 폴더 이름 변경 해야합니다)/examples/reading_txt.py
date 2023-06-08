#-*- coding:utf-8 -*-
import urllib as url

#url 인코딩 되어있는 list에 대해 url 디코딩과정과 파일리딩을 위한 코드.
def url_decode(return_text):
    with open('/home/pi/Adafruit_Python_SSD1306/examples/list','r') as file:
        text = file.readlines()
        for i in text:
            return_text.append((url.unquote(i)).replace('\r\n',''))
    return return_text

decoded_text = list()
url_decode(decoded_text)
print(decoded_text)

