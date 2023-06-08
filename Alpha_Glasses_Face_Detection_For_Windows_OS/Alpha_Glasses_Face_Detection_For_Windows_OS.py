#-*-coding:utf-8 -*-
import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from gtts import gTTS
import os
import time


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    
#xml파일열어서 얼굴 인식하는거 
#사람의 얼굴을 인식할 수 있도록 훈련되어있음.

#학습하는 함수
def train(name):
    data_path = 'data/user/' + name + '/'
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
        print(name + " 폴더에 사진이 없습니다.")
        return None
    Labels = np.asarray(Labels, dtype=np.int32)
    #모델 생성   
    model = cv2.face.LBPHFaceRecognizer_create()
    #학습!
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    print(name + " : 학습 완료!")

    #모델 리턴
    return model


def trains():
    #
    data_path = 'data/user'
    # 
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
    
    #폴더만 찾아냄 data/user아래의 -> 즉 사용자 폴더를 찾아내는 것
    models = {}
    # 
    for model in model_dirs:
        print('트레이닝 대상 모델 :' + model)
        
        result = train(model)
         
        if result is None:
            continue
         
        
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
        return img,roi   #검출된 좌표에 사각 박스 && 검출된 부위를 잘라(roi) 전달

        #얼굴에 대한 위치를 찾아 얼굴에 대한 네모박스를 그림.
        #손 쉬운 처리를 위해서 사이즈를 줄이고 흑백으로 바꿈.
def run(models):
        
        
        
        
        i=1
        while(i==1): #원래 whlie(ture)였는데 -> 한번만 실행시키고 싶어서 고침 -\
            i=0#한번실행하도록 바꾼거
            
            #os.system('raspistill -o test.jpg')#라즈베리 파이 카메라 실행시키는 명령어 
            #ret, frame = cap.read() 비디오 받아오는거 
            #cv2.imwrite('test.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0]) 
            frame = cv2.imread('test.jpg', cv2.IMREAD_COLOR)#라파로 찍은 이미지 불러옴
            #img_r = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)#이미지 회전 -> 시계 반대방향으로
            #cv2.imwrite('user.jpg', img_r, params=[cv2.IMWRITE_PNG_COMPRESSION,0])# 저장
            #frame = cv2.imread('user.jpg', cv2.IMREAD_COLOR)#다시 읽어옴
            image, face = face_detector(frame)# 
            
            try:   
                min_score = 999#적을수록 가까움, 닮은 정도    
                min_score_name = ""   #이름       
             
            
           
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #흑백
                #누구인지 판별
                for key, model in models.items():
                    result = model.predict(face)                
                    if min_score > result[1]:
                        min_score = result[1]
                        min_score_name = key
                    
                #적을수록 일치율이 높음
                if min_score < 500:
               
                    confidence = int(100*(1-(min_score)/300))#일치율 계산식
                if(confidence > 75):#일치율 75%이상이면 맞다고 판단
                
                    print(min_score_name)#윈도우에서만 필요!
                    print(str(confidence)+'%')
                    break
                
                #
                
           
          
            
               
                else:
                    print('저장된 사진이 없습니다. unknown')
                    min_score_name = "unknown"#얼굴은 인식했으나 맞는 사람이 없을때 대상의 이름을 unknown이라판단
                    break
            except:
                #얼굴 감지가 안됐을 때 뜨는 것들
                print('얼굴이 감지되지 않았습니다 대상을 다시 찍어주세요!')
                text = "얼굴이 감지되지 않았습니다 대상을 다시 찍어주세요!"
                tts = gTTS(text=text, lang='ko')
                tts.save("noface"+ ".mp3")
                os.system('noface'+'.mp3')
                exit()
                    
            if cv2.waitKey(1)==13:#특정 키 눌렀을때 종료 라파에선 안쓸듯 
                break    
          
                  
    
               
 
        try:#판단한 사람의 txt파일을 불러옴
            f = open("data/"+min_score_name+"/info.txt", mode='rt', encoding='utf-8')
            text = f.read()
        except:#만약 없으면 없다고 뜨는 것
            
            
            text1 = '폴더에 대상에 대한 정보가 저장되지 않았습니다'
            text = min_score_name + ' ' + text1
            
        
        #tts실행
        slow1 = True
        tts = gTTS(text=text, lang='ko', slow = slow1)
        tts.save(min_score_name+ ".mp3")
        f.close()
        #mp3파일 실행 라파에선 다르게~
        os.system(min_score_name+'.mp3')
        f = open(min_score_name + "/info.txt", mode='rt', encoding='utf-8')
        while True:#info를 읽어오는 코드
            user = f.readline()
            if not user:
                break
            print(user)
        f.close()
        print("\n")
                
        
        cap.release()
        cv2.destroyAllWindows()#윈도우에서 창 다 지우는 것

if __name__ == "__main__":
    #
    models = trains()
    #
    run(models)