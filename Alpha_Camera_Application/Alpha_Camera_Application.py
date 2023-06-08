# -*-utf-8 -*-

import cv2
import numpy as np
from os import makedirs
from os.path import isdir
import os
import time
import shutil


face_dirs = 'img/'

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#사람의 얼굴을 학습한 파일
#얼굴 검출하는 거!
def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None
    # 얼굴 찾으면 검출해서 자름
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    # 자른거 리턴
    return cropped_face
  


def take_pictures(name):
    
    if not isdir(face_dirs+name):#face_dir -> 경로 img/
        makedirs(face_dirs+name)        
    if not isdir(face_dirs+'tmp'):#face_dir -> 경로 img/
        makedirs(face_dirs+'tmp')
        
    cap = cv2.VideoCapture(0)#사진 찍음
    count = 0
    c=0
    while True: #무한반복함
        
        ret, frame = cap.read()
        # 비디오 한 프레임 따오는거 걍 사진이라고 생각해라 친구들아
        #얼굴 있으면 작용
        if face_extractor(frame) is not None:
            #c+=1 
            count+=1
            # 사진의 사이즈를 200*200으로 자름
            face = cv2.resize(face_extractor(frame),(200,200))
            # 흑백으로 변환
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # 자른 사진을 저장 user+n으로 저장(단! n은 자연수)
            file_name_path = face_dirs + 'tmp' + '/user'+str(count)+'.jpg'
            print(str(count)+'번째 사진이 찍혔습니다!')
            cv2.imwrite(file_name_path,face)
            #사진 몇장 찍었는지 보여줌
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
            
        else:
            
            print("카메라에서 멀리 떨어지거나 가까이 다가와 보세요")#얼굴 안나왔을때 말하는거 (라파에선 없을거임)
            time.sleep(0.1)
            pass
        
        # 얼굴 사진 100장 다 찍으면 종료!아니면 enter키 
        if cv2.waitKey(1)==13 or count==100:
            break

    cap.release()
    cv2.destroyAllWindows()
    print('사진 100장이 '+name+'폴더에 저장되었습니다!')


if __name__ == "__main__":
    print('곧 사진 촬영을 시작합니다.\n')
    print('알맞은 자리에서 카메라를 응시하여 주시기 바랍니다.\n')
    print('화면에 뜨는 본인의 얼굴이 맞는지 확인하시고 촬영이 끝났을 때,\n\n입력한 이름으로 저장된 사진들을 확인하여 주기시 바랍니다.\n')
   

    
    # 사진 저장할 이름을 넣어서 함수 호출
    a=input('사람 이름을 입력해주세요.(한글과 영어 모두 가능합니다) :')
    print('\n3초후 사진 촬영을 시작합니다.\n')
    print('3...\n')
    time.sleep(1)
    print('2...\n')
    time.sleep(1)

    print('1...\n')
    time.sleep(1)
    print('촬영 시작!\n')

    
    take_pictures(a)
    count = 0
    while True:#한글도 지원할 수 있도록 tmp디렉토리에서 사진들을 옮김
        count+=1
        file_name_path = face_dirs + 'tmp' + '/user'+str(count)+'.jpg'
        tmpdir = face_dirs + a + '/user'+str(count)+'.jpg'
        shutil.move(file_name_path, tmpdir)
        if count==100:
            break

    time.sleep(2)
