# Alpha Glasses
## Alpha Glasses에 들어가는 모든 프로그램들의 설명을 기재한 곳입니다.
- 실제 사용되는 모든 프로그램들의 코드와 실행 파일들을 올려두었습니다. 각각의 프로그램들의 구동 OS와 같은 환경들은 각각의 프로그램들에 기재하도록 하겠습니다.
- 제품 개발에 사용된 논문들과 제작한 보고서들 또한 원본을 Appendix 폴더에 넣어 제출하겠습니다.
- Raspbian에 내장되는 인공지능, 화면 출력 소스코드는 모두 Alpha_Glasses_Face_Detection&Transparent_Display_Output 디렉토리 내부의 Alpha 디렉토리 내부의 examples 디렉토리에 있습니다. 각각의 파일 명들은 아래 Transparent Display Output 부분에서 설명이 되고 있습니다.

## Alpha Glasses Face Detection A.I (For Raspbian Os Attached Raspberry Pi Zero WH)
- 제작 언어: Python3
- 구동 OS: Raspbian
- 구동 하드웨어: Raspberry Pi Zero WH
- 구동에 필요한 라이브러리:
```
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install numpy
pip3 install gTTS
```
- Raspbian이 설치된 Raspberry Pi Zero WH에서 구동하기 위해 제작된 프로그램으로 일반적인 Windows 환경에서는 구동되지 않습니다.
- Transparent Display  Output 프로그램과 모듈화 되어 있기에 함께 구동하지 않으면 정상적으로 작동 되지 않습니다.

## Alpha Glasses Face Detection A.I (For Windows OS)
- 제작 언어: Python
- 버젼 : 3.7.8
- 구동 OS: Windows
- 제작과 구동을 테스트 한 하드웨어: Samsung Odyssey Z
- 구동에 필요한 라이브러리:
```
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install numpy
pip3 install gTTS
```
- 인공지능을 구동하실 수 없는 Windows 환경에서도 구동을 해보실 수 있도록 Windows 환경에서 구동가능한 버전을 따로 만들었습니다.
- Windows OS 구동용은 따로 Transparent Display Output 프로그램이 존재하지 않아 오직 콘솔에만 결과가 나타납니다.
- 라즈베리 파이에서 구동시킬 때는 사진이나 정보가 자동으로 알맞은 경로에 저장되지만, 
  윈도우의 경우에는 인식할 대상을 data/user 폴더 아래에 대상의 이름으로된 폴더를 생성하여(ex : 위승빈)
  그 폴더 안에 100장의 사진과 대상의 정보를 적은 info.txt파일을 수동으로 저장해 주셔야합니다. 
  
## Transparent Display Output
- 제작 언어: Python3
- 구동 OS: Raspbian
- 구동 하드웨어: Spark fun Transparent OLED LCD-15173 / Raspberry Pi Zero W
- 구동에 필요한 라이브러리: 
```
git clone https://github.com/adafruit/Adafruit_SSD1306
pip install urllib
```
- real.py / reading_txt.py / image.py / button.py /4개의 파일로 출력 관련 부분을 담당하고 있습니다.
- real.py - 모든 모듈, 인공지능을 불러오는 역할을 맡고 있으며, 실질적인 출력이 이뤄지는 파일입니다.(GPIO.BOARD Mode)
- reading_txt.py - 웹서버에서 받은 url인코딩이 되어있는 텍스트에 대해 디코딩된 문자열을 반환하는 파일입니다.
- image.py - ppm 파일을 출력하기 위한 함수를 내장한 파일입니다.(GPIO.BOARD Mode)
- button.py - 버튼을 통한 하드웨어 입출력 여부를 확인하는 파일입니다.(GPIO.BCM Mode)
- 위 파일들은 모두 파이썬 2.x 버전을 이용하므로, 개별실행을 원하신다면 python3가 아닌 python 명령어를 통해 실행하셔야 합니다.
- image.py와 real.py는 같은 GPIO핀에 대해 같은 모드를 공유하지만, button.py는 별도로 돌아갑니다.(하드웨어적인 문제.)
- GPIO핀의 모드가 다른것을 이용하여, import과정에서 한번에 한가지의 모드만 쓸수있으므로, 추가적인 호출없이도 버튼 입력을 체크할 수 있습니다.
- start_shell.sh 파일을 rc.local 파일에 등록하고 사용하면, 전원 인가 후 버튼만 누르면 바로 동작합니다.
   
## Alpha Camera Application (Code)
- 제작 언어: Python
- 버젼: 3.7.8
- 구동 OS: Windows
- 제작과 구동을 테스트 한 하드웨어: Samsung Odyssey Z
- 구동에 필요한 라이브러리: 
```
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install numpy
```
- 이 코드를 pyinstaller를 통해 exe 파일로 만든 것이 Alpha Camera Application (Program) 입니다.
- 코드를 실행시키면 img폴더 아래 입력한이름의 폴더가 생성되며, 그 폴더 안에는 촬영된 100장의 사진이 들어있습니다.

## Alpha Camera Application (Program)
- 제작 언어: Python
- 버젼:  3.7.8
- PyInstaller: 4.0
- 구동 OS: Windows
- 제작과 구동을 테스트 한 하드웨어: Samsung Odyssey Z
- zip파일에 .exe파일과 구동에 필요한 모든 파일들을 함께 저장해서 사용자가 따로 라이브러리 파일을 설치하지 않아도 실행 가능합니다.

## Alpha Glasses Manageing Website
- 제작 언어: Node.js
- 서비스 중인 서버 OS: Raspbian
- 제작과 구동을 테스트 한 하드웨어: Samsung Odyssey Z
- 실제 구동되고 있는 하드웨어: Raspberry Pi 4
- 구동에 필요한 패키지:
```
pip install node
```
- 구동 방법:
```
sudo node index.js
```
- or
```
sudo nodemon
```

## Appendix
- Alpha Glasses 제작에 사용된 문서들의 원본들 입니다.
- ALFA 기억법 제작 보고서.pdf
- 고령자, 치매 작업 치료학회지.pdf
- 이석범, 김기웅 - 알츠하이머병에 대한 비약물적 개입.pdf