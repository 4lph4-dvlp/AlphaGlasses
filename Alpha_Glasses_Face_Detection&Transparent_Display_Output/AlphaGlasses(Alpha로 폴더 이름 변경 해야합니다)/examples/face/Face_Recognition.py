#-*- coding:utf-8 -*-
import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from gtts import gTTS
import os
import time


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    
#xml파일열어서 얼굴 인식하는거  
#학습하는 함수
def train(name):
    data_path = 'data/user' + name + '/'
    #data가 들어있는 주소 -> data_path
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path,f))]
    
    Training_Data, Labels = [], []
    
    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
       
        if images is None:
            continue    
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    if len(Labels) == 0:
        print(name + " 폴더에 사진이 없습니다.")
        return None
    Labels = np.asarray(Labels, dtype=np.int32)
   
    model = cv2.face.LBPHFaceRecognizer_create()
   
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    print(name + " : 학습 완료!")

    
    return model


def trains():
    #
    data_path = 'data/user'
    # 
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
    
    #
    models = {}
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
        return img,roi   #


def run(models):
        
        
        
        
        i=1
        while(i==1): #원래 whlie(ture)였는데 -> 한번만 실행시키고 싶어서 고침 -\
            i=0
            cap = cv2.VideoCapture(0)
            #os.system('raspistill -o test.jpg')#라즈베리 파이 카메라 실행시키는 명령어 
            ret, frame = cap.read()
            cv2.imwrite('test.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
            frame = cv2.imread('test.jpg', cv2.IMREAD_COLOR)#라파로 찍은 이미지 불러옴
            #img_r = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)#이미지 회전 -> 시계 반대방향으로
            #cv2.imwrite('user.jpg', img_r, params=[cv2.IMWRITE_PNG_COMPRESSION,0])# 저장
            #frame = cv2.imread('user.jpg', cv2.IMREAD_COLOR)#다시 읽어옴
            image, face = face_detector(frame)# 
            
            try:   
                min_score = 999    
                min_score_name = ""         
             
            
           
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    
                for key, model in models.items():
                    result = model.predict(face)                
                    if min_score > result[1]:
                        min_score = result[1]
                        min_score_name = key
                    
               
                if min_score < 500:
               
                    confidence = int(100*(1-(min_score)/300))
                if(confidence > 75):
                
                    print(min_score_name)
                    print(str(confidence)+'%')
                    break
                
                #
                
           
          
            
               
                else:
                    print('저장된 사진이 없습니다. unknown')
                    min_score_name = "unknown"
                    break
            except:
            
                print('얼굴이 감지되지 않았습니다 대상을 다시 찍어주세요!')
                text = "얼굴이 감지되지 않았습니다 대상을 다시 찍어주세요!"
                tts = gTTS(text=text, lang='ko')
                tts.save("noface"+ ".mp3")
                os.system('noface'+'.mp3')
                exit()
                    
            if cv2.waitKey(1)==13:
                break    
          
                  
    
               
 
        try:
            f = open("data/"+min_score_name+"/info.txt", mode='rt', encoding='utf-8')
            text = f.read()
        except:
            
            f = open("try.txt", mode='rt', encoding='utf-8')
            text1 = f.read()
            text = min_score_name + ' ' + text1
            
        
    
        tts = gTTS(text=text, lang='ko')
        tts.save(min_score_name+ ".mp3")
        f.close()

        os.system(min_score_name+'.mp3')
        f = open(min_score_name + "/info.txt", mode='rt', encoding='utf-8')
        while True:
            user = f.readline()
            if not user:
                break
            print(user)
        f.close()
        print("\n")
                
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    #
    models = trains()
    #
    run(models)
