from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import pyautogui
import requests

options = webdriver.ChromeOptions()

# headless 옵션 설정
# options.add_argument('headless')  # 창 숨기는 옵션
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")  # 가속 사용 x
options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 크롬 드라이버 최신 버전 설정
service = ChromeService(executable_path='./chromedriver-win64/chromedriver.exe')

# chrome driver
driver = webdriver.Chrome(service=service, options=options)
print(driver.capabilities['browserVersion'])

driver.maximize_window()

# NVIDIA 로그인 대기 로직 시작 ---------------------------------------------------------------------
nvidiaUrl = 'https://accounts.shopify.com/lookup?rid=84809cae-ea1a-4c72-8475-bf7561f26877'              #####################################################################################################수정한 부분
uploadUrl = 'https://nidvia.co.kr/api/qr/upload'  # Server
# uploadUrl = 'http://localhost:3000/api/qr/upload'     # TEST Local
qrImageFileName = 'nvidia_signin_with_qr.png'

while True:
    # Nvidia 접속
    driver.get(nvidiaUrl)
    driver.implicitly_wait(time_to_wait=5)  # 5초까지 기다려 준다 (파싱되는 시간을 기다려준다)

    # 로그인 버튼 찾아 클릭
    loginLink = driver.find_element(By.ID, 'web_authn_btn_trigger')          #####################################################################################################수정한 부분
    loginLink.click()

    # 로그인 페이지 화면 로딩 대기
    driver.implicitly_wait(time_to_wait=5)  # 5초까지 기다려 준다 (파싱되는 시간을 기다려준다)

    print(driver.current_url)  # 현재 URL 출력
    print(driver.title)  # 현재 웹 페이지 제목 출력

    # 보안 장치로 로그인 버튼 찾아 클릭
    #signInLink = driver.find_element(By.ID, 'signIn_withSecurityDevice_link')      #####################################################################################################수정한 부분
    #signInLink.click()                                                             #####################################################################################################수정한 부분
    
    time.sleep(3)  # 무조건 3초 대기

    # 마우스 클릭 QR 코드 (다른 휴대전화 또는 테블릿 사용)
    print(pyautogui.position())  # 현재 마우스 위치 출력
    pyautogui.moveTo(600, 470)  # 버튼 위치로 이동
    pyautogui.click()           # 클릭

    time.sleep(1)  # 무조건 1초 대기

    # QR 코드 상단 이미지 위치 확인
    qrLocation = pyautogui.locateOnScreen('qr_sample.png')  # 이미지가 있는 위치를 가져옵니다.

    # QR 코드 화면 캡쳐
    nvidiaQrImage = pyautogui.screenshot(qrImageFileName, region=(1057, 77, 445, 445))

    # files = open('nvidia_signin_with_qr.png', 'rb')
    qrCaptureImageFile = open(qrImageFileName, 'rb')
    uploadFiles = {'file': (qrImageFileName, qrCaptureImageFile, 'image/png')}
    # headers = {'Content-Type' : 'image/jpeg'}

    print(uploadFiles)
    res = requests.post(uploadUrl, files=uploadFiles)

    print("파일 전송 결과: {}".format(res.status_code))

    # driver.get_screenshot_as_file('nvidia_signin_with_qr.png')    # 웹 화면캡처

    time.sleep(60)  # 무조건 60초 대기

    # 현재 퓁 페이지 제목으로 로그인 되었는지 체크
    # 로그인 되었다면 사용자 정보 취득 하고 종료
    if driver.title == "로그인 성공":
        print("개인 정보 취득 성공")
        break


driver.quit()  # driver 종료
print("종료")

