# [Python] Selenium(셀레니움) 


## Selenium 이란?
> 셀레니움의 원래 용도는 웹 테스트 자동화 프레임워크이다. 
> selenium webdriver를 이용하여 다양한 브라우저를 조종할 수 있다. 
> 셀레니움은 구글 크롬, 파이어폭스, 사파리, 마이크로소프트 엣지등의 브라우저를 조종할 수 있는 
> 웹드라이버를 통하여 작동하기 때문에 웹 UI나 기능 테스트에 주로 사용한다.

BeautifulSoup 같은 다른 웹 수집기도 있지만 이러한 수집기들은 Javascript로 실행하는 비동기적인 컨텐츠(뒤 늦게 불려와지는 컨텐츠)들은 수집하기 어려운 단점이 있다. 셀레니움을 크롤러로 사용했을 때 웹드라이버를 통하여 실제 사람이 사용하는 것과 비슷하게 작동하기 때문에 이미 페이지가 렌더링 된 상태에서 원하는 페이지의 html 파일을 수집할 수 있다. (html 파일에는 수집하고자 하는 다양한 정보들이 들어있다.)
아직 많이 사용해 보지 않아서 정확한 단점은 알 수 없지만 처음 사용해 봤을 때 느낀 점은 수집이 느리다는 단점이 있었다. 하지만 보이는 곳 어디든 수집이 가능하다는 장점이 있다.

--- 
## Selenium 설치
셀레니움은 pip를 이용하여 간단하게 설치할 수 있다. 그리고 페이지를 랜더링 한 후 html을 파싱해올 때 BeutifulSoup4를 사용하므로 만약에 설치되어 있지 않다면 같이 설치해준다.
* Selenium 설치 
  - [홈페이지 침고](https://pypi.org/project/selenium/)
```shell
$ pip install selenium
```

* BeutifulSoup4 설치 
  - [홈페이지 참고](https://pypi.org/project/beautifulsoup4/) 
  - [뷰티플수프 4.0.0 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/)
```shell
$ pip install beautifulsoup4
```

* 크롬 브라우저 설치 및 크롬 웹드라이버 다운로드  

우선 셀레니움은 WebDriver를 이용하여 작동하는데 많이 사용하는 크롬 웹드라이버를 사용하여 작동할 예정이다.
운영체제 환경마다 셋팅하는 방법이 조금씩 다르다.
크롬 웹드라이버를 이용하므로 반드시 크롬 브라우저는 설치되어 있어야 한다!

아래의 주소에서 크롬 드라이버를 다운로드 받을 수 있다(GUI 환경)

[최신 크롬 드라이버 다운로드 페이지](https://googlechromelabs.github.io/chrome-for-testing/)  
https://googlechromelabs.github.io/chrome-for-testing/ 

> 프로젝트에 사용된 chromedriver	win64  	
> https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.92/win64/chromedriver-win64.zip	

 



---
## Selenium 기본 명령어

### 1. Selenium으로 DOM요소 선택 - 요소를 찾지 못하면 NoSuchElementException 발생

| 이름 | 설명 |
|---|---|
|처음요소를 추출||
|find_element_by_id(id)|id속성으로 요소를 하나 추출|
|find_element_by_name(name)|name 속성으로 요소를 하나 추출|
|find_element_by_css_selector(query)|css 선택자로 요소를 하나 추출|
|find_element_xpath(query)|xpath를 지정해 요소를 하나 추출|
|find_element_by_tag_name(name)|태그 이름이 name에 해당하는 요소를 하나 추출|
|find_element_by_link_text(text)|링크 텍스트로 요소를 추출|
|find_element_by_partial_link_text(text)|링크의 자식 요소에 포함되 있는 텍스트로 요소를 하나 추출|
|find_element_by_class_name(name)|클래스 이름이 name에 해당하는 요소를 하나 추출|
|모든 요소를 추출(element 뒤에 s가 붙는다.)|
|find_elements_by_css_selector(query)|css 선택자로 요소를 여러개 추출|
|find_elements_by_xpath(query)|xpath를 지정해 요소를 여러개 추출|
|find_elements_by_tag_name(name)|태그이름이 name에 해당하는 요소를 여러개 추출|
|find_elements_by_class_name(name)|클래스 이름이 name에 해당하는 요소를 여러개 추출|
|find_elements_by_partial_link_text(text)|링크의 자식 요소에 포함돼 있는 텍스트로 요소를 여러개 추출|


### 2. Selenium으로 요소를 조작하기

|메서드/ 속성|설명|
|---|---|
|clear()|글자를 지운다|
|click()|요소를 클릭|
|get_attribute(name)|요소 속성중 name에 해당하는 속성 값을 추출|
|is_displayed()|요소가 화면에 출력되는지 확인|
|is_enabled()|요소가 활성화돼 있는지 확인|
|is_selected()|체크박스 등의 요소가 선택된 상태인지 확인|
|screenshot(filename)|스크린샷|
|send_keys(value)|키를 입력|
|submit()|입력 양식을 전송|
|value_of_css_property(name)|name에 해당하는 css속성 값을 추출|
|id|id|
|location|요소의 위치|
|parent|부모요소|
|rect|크기와 위치 정보를 가진 사전자료형 리턴|
|screenshot_as_base64|스크린샷을 base64로 추출|
|screenshot_as_png|스크린샷을 png형식의 바이너리로 추출|
|size|요소의 크리|
|tag_name|태그 이름|
|text|요소의 내부 글자|


### 3. send_key()에서 특수키 입력

```python
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome("./chromedriver-win64/chromedriver", options=options)
driver.implicitly_wait(10)
driver.get('http://kind.krx.co.kr/disclosure/details.do?method=searchDetailsMain')

selected_tag_a=driver.find_element_by_css_selector('input#fromDate')

selected_tag_a.send_keys(Keys.BACKSPACE)

# ARROW_DOWN / ARROW_LEFT / ARROW_RIGHT / ARROW_UP BACKSPACE / DELETE / HOME / END /INSERT /
# ALT / COMMAND / CONTROL / SHIFT ENTER / ESCAPE /SPACE / TAB F1 / F2 / F3 ............./ F12
```


### 4. Selenium 드라이버 조작

|명령어|설명|
|---|---|
|add_cookie( cookie_dict)|쿠키값을 사전 형식으로 지정|
|back() / forward()|이전 페이지/ 다음페이지|
|close()|브라우저 닫기|
|current_url|현재 url|
|delete_all_cookies()|모든 쿠키 제거|
|delete_cookie(name)|name에 해당하는 쿠키 제거|
|execute( command, params)|브라우저 고유의 명령어 실행|
|execute_async_script( script, *args)|비동기 처리하는 자바스크립트를 실행|
|execute_script( script, *args)|동기 처리하는 자바스크립트를 실행|
|get(url)|웹 페이지를 읽어들임|
|get_cookie( name)|특정 쿠키 값을 추출|
|get_cookies()|모든 쿠키값을 사전 형식으로 추출|
|get_log(type)|로그를 추출(type: browser/driver/client/server)|
|get_screenshot_as_base64()|base64형식으로 스크린샷을 추출|
|get_screenshot_as_file(filename)|스크린샷을 파일로 저장|
|get_screenshot_as_png()|png형식으로 스키란샷의 바이너리를 추출|
|get_window_position(windowHandle='current')|브라우저의 위치를 추출|
|get_window_size( windowHandle='current')|브라우저의 크기를 추출|
|implicitly_wait(sec)|최대 대기 시간을 초 단위로 지정해서 처리가 끈날때 까지 대기|
|quit()|드라이버를 종료 시켜 브라우저 닫기|
|save_screenshot(filename)|스크린샷 저장|
|set_page_load_timeout( time_to_wait)|페이지르르 읽는 타임아웃 시간을 지정|
|set_script_timeout(time_to_wait)|스크립트의 타임아웃 시간을 지정|
|set_window_position(x,y,windowHandle='current')|브라우저 위치를 지정|
|set_window_size(width, height, windowHandle='current')|브라우저 크기를 지정|
|title|현재 타이틀을 추출|
 

 ---

## Selenium 사용해보기
 

### import
```python
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
```
 

### 브라우저 열기 (Chrome)
```python
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome("./chromedriver-win64/chromedriver", options=options)

driver.get("크롤링 할 주소 입력")
```

> 만약 코드를 실행 후 브라우저 창이 바로 닫힌다면 VSC와 셀레니움 사이에 무언가 호환이 잘 안되는 것 같다.
> 그럴 경우에는 현재 셀레니움 버전을 삭제 후 다른 버전의 셀레니움을 설치해주면 된다.
> 다시 재설치 이후 실행하면 브라우저 창이 계속 유지된다.

```shell
$ pip uninstall selenium

$ pip install selenium==3.141.0
```



### 브라우저 탭 이동/ 앞으로, 뒤로 / 닫기
* 탭 이동
```python
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome("./chromedriver-win64/chromedriver", options=options)

driver.window_handles[0] #브라우저 탭 객체를 리스트로 반환. [0] 은 첫번재 탭을 의미 
driver.switch_to.window(driver.window_handles[0]) #첫번째 탭으로 이동 
driver.switch_to.window(driver.window_handles[1]) #두번째 탭으로 이동 
driver.switch_to.window(driver.window_handles[2]) #세번째 탭으로 이동
```

* 뒤로가기 / 앞으로가기
```
driver.back() 	 #뒤로가기
driver.forward() #앞으로가기
```

* 탭닫기 / 브라우저 닫기
```
driver.close()   #현재 탭 닫기
driver.quit()    #브라우저 닫기
```
 

### 요소 선택
원하는 부분의 xpath 등을 가져와서 클릭하여 페이지 이동과 같은 행동을 할 수 있다.


* xpath 로 접근
``` python
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a')
```

* class 속성으로 접근
``` python
driver.find_element_by_class_name('nav')
```

* id 속성으로 접근
``` python
driver.find_element_by_id('search_btn')
```

* 링크가 달려 있는 텍스트로 접근
``` python
driver.find_element_by_link_text('회원가입')
```

* css 셀렉터로 접근
``` python
driver.find_element_by_css_selector('#gnb > div > > ul > li > a')
```

* name 속성으로 접근
``` python
driver.find_element_by_name('sform')
```

* 링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
``` python
driver.find_element_by_partial_link_text('가입')
```

* 태그 이름으로 접근
``` python
driver.find_element_by_tag_name('input')	
```

* input 태그 하위태그인 a 태그에 접근
``` python
driver.find_element_by_tag_name('input').find_element_by_tag_name('a')  
```

* xpath 로 접근한 엘레먼트의 안에 join 이라는 속성을 가진 tag 엘레먼트에 접근
``` python
driver.find_element_by_xpath('/html/body/div[3]/form//span[2]').find_element_by_name('join')
```

### 클릭
``` python
driver.find_element_by_xpath('//*[@id="main-area"]/div[7]/a[2]').click()
```
 

### 텍스트 입력/엔터
``` python
driver.find_element_by_name('query').send_keys('월드컵')
driver.find_element_by_name("query").send_keys(Keys.ENTER)
```
 

### 텍스트 삭제
``` python
driver.find_element_by_name("query").clear()
```
 

### iframe 지정
* iframe 지정
``` python
element = driver.find_element_by_tag_name('iframe')
```

* 프레임 이동
``` python
driver.switch_to.frame(element)
```

* 프레임에서 빠져나오기
``` python
driver.switch_to.default_content()
```
 

### 팝업창 이동 / 수락 / 거절
* 경고창으로 이동
``` python
driver.switch_to.alert

from selenium.webdriver.common.alert import Alert

Alert(driver).accept()    #경고창 수락 누름
Alert(driver).dismiss()   #경고창 거절 누름
print(Alert(driver).text  # 경고창 텍스트 얻음
```
 

### 스크롤 내리기
* 브라우저 스크롤 최하단으로 이동
``` python
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
```
 

### 스크린샷
* 캡쳐할 엘레먼트 지정
``` python
element = driver.driver.find_element_by_class_name('ico.target')
```

* 캡쳐 (name에는 파일명)
``` python
element.save_screenshot('name.jpg')
```
 

### 오류 예외 처리 try , except문
클릭이나 프레임 이동시 에러가 발생 할 경우 사용할 수 있다

``` python
try:
    print('') #실행할 코드
    
except:
    pass #오류 발생시 실행할 코드
    pass를 사용하면 오류를 회피한다.

    
#예시
    try:
        name = driver.find_element_by_tag_name('table')
    
    except NoSuchElementException:   #except 오류문(해당 오류가 발생시 실행)
        print(" [예외 발생] 표 없음 ")
        continue
        
    except 오류문2:  #오류문 여러개 사용가능
    
    else:	#오류가 없을시 try문 다음으로 실행한다.
    	print('오류가 없어요')
```
    
 

### 여러가지 오류 모음
* NoAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음
* NoSuchElementException 엘레먼트 접근하였으나 없음
* TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음
* ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님
* NoSuchWindowException 해당 윈도우 없음
* NoSuchFrameException 해당 프레임 없음# macro_py
