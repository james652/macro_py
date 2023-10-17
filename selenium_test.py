from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()

# headless 옵션 설정
# options.add_argument('headless')  # 창 숨기는 옵션
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 크롬 드라이버 최신 버전 설정
service = ChromeService(executable_path='./chromedriver-win64/chromedriver.exe')

# chrome driver
driver = webdriver.Chrome(service=service, options=options)  # <- options로 변경
print(driver.capabilities['browserVersion'])

driver.get('https://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('capture_naver.png')    # 화면캡처

driver.implicitly_wait(time_to_wait=5)      # 5초까지 기다려 준다

print(driver.current_url)
print(driver.title)

driver.quit() # driver 종료
