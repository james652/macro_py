from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import pyautogui


options = webdriver.ChromeOptions()
# headless 옵션 설정
# options.add_argument('headless')  # 창 숨기는 옵션
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")  # 가속 사용 x
options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 크롬 드라이버 최신 버전 설정
service = ChromeService(executable_path='./chromedriver-win64/chromedriver.exe')

def GetQR():
    # chrome driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # NVIDIA 로그인 대기 로직 시작 ---------------------------------------------------------------------
    nvidiaUrl = 'https://www.nvidia.com/ko-kr/account/'
    qrImageFileName = 'nvidia_signin_with_qr.png'

    # Nvidia 접속
    driver.get(nvidiaUrl)
    driver.implicitly_wait(time_to_wait=3)  # 5초까지 기다려 준다 (파싱되는 시간을 기다려준다)

    # 보안 장치로 로그인 버튼 찾아 클릭
    signInLink = driver.find_element(By.ID, 'signIn_withSecurityDevice_link')      #####################################################################################################수정한 부분
    signInLink.click()                                                             #####################################################################################################수정한 부분
    time.sleep(3)  # 무조건 3초 대기

    # 마우스 클릭 QR 코드 (다른 휴대전화 또는 테블릿 사용)
    pyautogui.moveTo(1187, 360)  # 버튼 위치로 이동
    pyautogui.click()           # 클릭
    time.sleep(3)  # 무조건 1초 대기

    # QR 코드 화면 캡쳐
    # nvidiaQrImage = pyautogui.screenshot(qrImageFileName, region=(1055+12, 82+12, 450-24, 496-24)) # FIDO POPUP With QR
    pyautogui.screenshot(qrImageFileName, region=(1055+86, 82+134, 278, 278)) # Only QR

    time.sleep(20)  # 무조건 60초 대기

    if driver.title == "로그인 성공":
        print("개인 정보 취득 성공")

    # 현재 웹 페이지 제목으로 로그인 되었는지 체크
    # 로그인 되었다면 사용자 정보 취득 하고 종료
    driver.quit()  # driver 종료

