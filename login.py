from appium import webdriver
import os
#import subprocess
#from appium.options.android import UiAutomator2Options
from appium.options.common.base import AppiumOptions
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction
import subprocess


appium_server = 'http://localhost:4723/wd/hub'

seoltab_app_package = 'com.seoltab.seoltab'
seoltab_app_activity = 'com.seoltab.seoltab.MainActivity'


desired_caps = {
    "platformName": "Android",
	"deviceName": "R54W104V3QY",
	"appPackage": seoltab_app_package,
	"appActivity": seoltab_app_activity,
	"ensureWebviewsHavePages": True,
	"nativeWebScreenshot": True,
	"newCommandTimeout": 3600,
	"connectHardwareKeyboard": True, 
    "autoGrantPermissions" : True # 자동으로 권한 부여
}

#option = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, desired_caps)
wait = WebDriverWait(driver, 20)
find = driver.find_element

# 테스트 계정
test_id = "jaden_s1@seoltab.test"
test_pw = "asdfasdf"
print('로그인/로그아웃 테스트를 시작합니다.')
print('테스트 계정 = ',test_id)

# 로그인
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc=\"이메일\n비밀번호\"]/android.widget.EditText[1]")))

log_text = find(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"로그인\"]") # log_text 에 element 지정
chck_text = log_text.tag_name # 'log_text' 에서 텍스트를 추출하여 'chck_text' 에 저장
print(chck_text,' 페이지에 정상 접속하였습니다.')

log_id = find(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"이메일\n비밀번호\"]/android.widget.EditText[1]")
log_id.click() # 로그인 ID 입력창 클릭
log_id.send_keys(test_id) # 로그인 ID 입력
log_pw = find(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"이메일\n비밀번호\"]/android.widget.EditText[2]")
log_pw.click() # 로그인 ID 입력창 클릭
log_pw.send_keys(test_pw) # 로그인 PW 입력
login_bt = find(by=AppiumBy.ACCESSIBILITY_ID, value="로그인").click() # 로그인 버튼 클릭

# 튜토리얼 컨트롤
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView")))
print('로그인이 정상적으로 완료 되었습니다.')


tc = 0
x_coordinate = 750  # 원하는 X 좌표
y_coordinate = 130  # 원하는 Y 좌표     

touch_action = TouchAction(driver) # TouchAction 객체 생성

tutorialElemValues = [
	"1",
	"2",
	"3",
]

try:
	for tutorialElemValue in tutorialElemValues:
		tutorialElem = find(by=AppiumBy.ID, value=tutorialElemValue)
		isTutorialExist = tutorialElem.is_displayed
		if(not isTutorialExist):
			raise Exception()
		touch_action.tap(x=x_coordinate, y=y_coordinate).perform()
		print('과외 튜토리얼 확인')

except:
    print("error")
	
 
 
	
#while t <= 12: # 지정한 좌표를 지정한 횟수 만큼 탭
#    touch_action.tap(x=x_coordinate, y=y_coordinate).perform()
#    print('튜토리얼을 컨트롤 중입니다.',t)
#    t += 1
#    sleep(1)

#과외_튜토리얼_이미지 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.view.View/android.widget.ImageView[1]")
#과외_튜토리얼_설명 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.view.View/android.widget.ImageView[2]")

# 로그아웃
gnb_my = find(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView")
gnb_my.click() # GNB 마이페이지 아이콘 클릭
wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.seoltab.seoltab:id/tvLogout"))) # 마이페이지에서 로그아웃 버튼을 찾을때까지 대기
my_logout = find(by=AppiumBy.ID, value="com.seoltab.seoltab:id/tvLogout")
my_logout.click() # 마이페이지 로그아웃 버튼 클릭

# 로그인 페이지 랜딩 성공 체크
wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "로그인"))) # 로그인 페이지로 랜딩 후 로그인 버튼을 찾을때까지 대기
log_text = find(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"로그인\"]")
chck_text = log_text.tag_name
print('정상적으로 로그아웃 하여 ', chck_text, '페이지로 이동 하였습니다.')
print('로그인/로그아웃 테스트 완료')

driver.quit()

print('OK. bye~')