#!/usr/bin/env python
# coding: utf-8

# In[41]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# WebDriver 객체 생성 (Chrome 드라이버 사용)
service = Service(executable_path='C:\chromedriver.exe')
driver = webdriver.Chrome(service=service)
#브라우저 창 최대화
driver.maximize_window()
#  로그인 페이지로 이동
driver.get('http://gw.camusenc.com/DeskPlusEIP/EIP/DeskPlusEPDefault.aspx')

# 아이디와 비밀번호 입력
id_input = driver.find_element(By.NAME,'tbLoginID')
id_input.send_keys('smlee9')  # 여기에  아이디를 입력하세요

pw_input = driver.find_element(By.NAME,'tbPassword')
pw_input.send_keys('1234')  # 여기에 비밀번호를 입력하세요

# 로그인 버튼 클릭
login_button = driver.find_element(By.ID,'Submit1')
login_button.click()
sleep(2)

pyautogui.moveTo(100,500)
pyautogui.click()
sleep(2)
pyautogui.click(x=60, y=638)


# In[ ]:




