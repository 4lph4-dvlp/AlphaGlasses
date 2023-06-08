import urllib as url

#def print_oled(return_text):
    #with open('word.txt','r') as file:
        #for text in file:
            #print(text.strip('\n'))
            #return_text.append(text)
    #return return_text

def url_decode(return_text):
    with open('list','r') as file:
        text = file.readlines()
        for i in text:
            return_text.append((url.unquote(i)).replace('\r\n',''))
    return return_text

decoded_text = list()
url_decode(decoded_text)
print(decoded_text)

