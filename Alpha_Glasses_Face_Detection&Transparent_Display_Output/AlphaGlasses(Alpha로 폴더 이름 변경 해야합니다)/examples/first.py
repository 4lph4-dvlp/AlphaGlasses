#-*- coding:utf-8 -*-
import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from subprocess import call
from gtts import gTTS
import os
import time

def start():
    face_classifier = cv2.CascadeClassifier('/home/pi/Adafruit_Python_SSD1306/examples/haarcascade_frontalface_default.xml')    
    #xml파일열어서 얼굴 인식하는거  
    #학습하는 함수
    def train(name):
        data_path = '/home/pi/Adafruit_Python_SSD1306/examples/data/user/' + name + '/'
        #data가 들어있는 주소 -> data_path
        face_pics = [f for f in listdir(data_path) if isfile(join(data_path,f))]
        #파일 -> 리스트 
        Training_Data, Labels = [], []
        
        for i, files in enumerate(face_pics):
            image_path = data_path + face_pics[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            #이미지가 아니면 지나감
            if images is None:
                continue    
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)
        if len(Labels) == 0:
        # if(len(Labels) == 1):
            # filename = os.listdir('/data/user'+name+'/')
            # print(filename+'\n')
            # print(len(filename)
                
                
            print(name + " 폴더에 사진이 없습니다.")
            return None
        Labels = np.asarray(Labels, dtype=np.int32)
        #모델 생성
        model = cv2.face.LBPHFaceRecognizer_create()
        #학습 
        model.train(np.asarray(Training_Data), np.asarray(Labels))
        print(name + " : 학습 완료!")

        
        return model
        #학습된 모델 리턴

    def trains():
        #
        data_path = '/home/pi/Adafruit_Python_SSD1306/examples/data/user/'
        # 
        model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
        #data/user 아래에 폴더를 찾음 -> 사용자 폴더 찾
        #
        models = {}음
        # 
        for model in model_dirs:
            print('트레이닝 대상 모델 :' + model)
            #
            result = train(model)
            # 
            if result is None:
                continue
            # 
            
            models[model] = result

        #
        return models    

    #얼굴 감지하는 함수
    def face_detector(img, size = 0.5):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            if faces is():
                return img,[]
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)

                roi = img[y:y+h, x:x+w]
                roi = cv2.resize(roi, (200,200))
            return img,roi   #검출된 자표에 네모 박스 && roi전달
            #얼굴에 대한 위치를 찾아 얼굴 주변에 네모박스 그림
            #효율성을 위해 사이즈를 줄이고 흑백으로 바꿈

    def run(models):
            
            path_of_data = '/home/pi/Adafruit_Python_SSD1306/examples/'
        
            
            i=1
            while(i==1): #원래 whlie(ture)였는데 -> 한번만 실행시키고 싶어서 고침 -\
                i=0
                print('5seconds')
                os.system('raspistill -o ' + path_of_data + 'test.jpg')#라즈베리 파이 카메라 실행시키는 명령어 
                print('찰칵!')
                #ret, frame = cap.read()
                #cv2.imwrite(path_of_data + 'test.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
                frame = cv2.imread(path_of_data + 'test.jpg', cv2.IMREAD_COLOR)#라파로 찍은 이미지 불러옴
                img_r = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)#이미지 회전 -> 시계 반대방향으로
                cv2.imwrite(path_of_data + 'user.jpg', img_r, params=[cv2.IMWRITE_PNG_COMPRESSION,0])# 저장
                frame = cv2.imread(path_of_data + 'user.jpg', cv2.IMREAD_COLOR)#다시 읽어옴
                image, face = face_detector(frame)# 
                
                try:   
                    min_score = 999    #적을수록 닮은 정도가 가까움
                    min_score_name = ""         
                
                
            
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    #흑백 
        
                    for key, model in models.items():
                        result = model.predict(face)                
                        if min_score > result[1]:
                            min_score = result[1]
                            min_score_name = key
                        
                
                    if min_score < 500:
                
                        confidence = int(100*(1-(min_score)/300))
                    if(confidence > 75):#일치율 75%이상이면 그 사람이라고 판단
                        print(min_score_name)
                        print(str(confidence)+'%')
                        break
                    
                    #
                    
            
            
                
                
                    else:
                        print('저장된 사진이 없습니다. unknown') #얼굴 인식 but 맞는 사람이 없을때는 unknown
                        min_score_name = "unknown"
                        break
                except:
                
                    print('얼굴이 감지되지 않았습니다') #사진에 얼굴이 없으면 실행
                    exit()
                    
                if cv2.waitKey(1)==13:#특정 키 누르면 종료
                    break    
            
                    
        
                
    
            try:#판한 사람의 txt파일을 불러옴
                f = open("/home/pi/Adafruit_Python_SSD1306/examples/data/user/" + min_score_name + "/info.txt", mode='rt', encoding='utf-8')
                text = f.read()
            except:
                
                
                text1 = '폴더에 대상에 대한 정보가 저장되지 않았습니다'
                text = min_score_name + ' ' + text1
                print(text)
            
             
            tts = gTTS(text=text, lang='ko')
            tts.save('/home/pi/Adafruit_Python_SSD1306/examples/'+ min_score_name+ ".mp3")
            f.close()
            #tts파일 실행
            #os.system('sudo aplay '+min_score_name+'.wav')
            call(['mplayer','/home/pi/Adafruit_Python_SSD1306/examples/'+  min_score_name+'.mp3'])
            f = open("/home/pi/Adafruit_Python_SSD1306/examples/data/user/" + min_score_name + "/info.txt", mode='rt', encoding='utf-8')
            while True:
                user = f.readline()
                if not user:
                    break
                print(user)
            f.close()
            print("\n")
                    
            
        #  cap.release()
        # cv2.destroyAllWindows()
            
    if __name__ == "__main__":
        #
        models = trains()
        #
        run(models)
start()
