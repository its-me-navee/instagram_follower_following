import xlwt
from time import sleep
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(1)
driver.maximize_window()

username='###'
password='###'

url = 'https://www.instagram.com/'

driver.get(url)

sleep(1)
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

# username = 'jo.hnparker283'
# password = 'qwasdzxplm1234'

username_input.send_keys(username)
password_input.send_keys(password)

login_button = driver.find_elements(By.XPATH, "//button[@type='submit']")
# print(login_button)
login_button[0].click()

sleep(10)

notnow_button = driver.find_elements(By.XPATH, "//button[@type='button']")
# print(notnow_button)
notnow_button[0].click()

sleep(10)

turnon_button = driver.find_elements(By.CLASS_NAME, "_a9--._a9_0")
# print(turnon_button)
turnon_button[0].click()

sleep(10)

profile = driver.find_elements(By.LINK_TEXT, username)
profile[0].click()

sleep(10)

following = driver.find_elements(By.PARTIAL_LINK_TEXT, 'following')
follower = driver.find_elements(By.PARTIAL_LINK_TEXT, 'follower')

following[0].click()

sleep(10)

lst = driver.find_elements(By.CLASS_NAME, 'x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1')
lstP = driver.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aad6._aade')

# for elem in lstP:
#     print(elem.text)

followingList = []
for i in range(len(lst)):
    if lstP[i].text == 'Follow':
        break
    name = lst[i].text.split('\n')
    print(name[0])
    followingList.append(name[0])

sleep(10)

driver.back()

follower[0].click()

sleep(10)

lst = driver.find_elements(By.CLASS_NAME, 'x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1')
lstP = driver.find_elements(By.CLASS_NAME, '_aacl._aaco._aacw._aad6._aade')

followerList = []
for i in range(len(lst)):
    if lstP[i].text == 'Follow':
        break
    name = lst[i].text.split('\n')
    followingList.append(name[0])

# print(followingList)
# print('\n')
# print(followerList)
# sleep(10)

accounts1, accounts2 = [], []

for nam in followingList:
    if nam not in followerList:
        accounts1.append(nam)

for nam in followerList:
    if nam not in followingList:
        accounts2.append(nam)

print("Accounts you follow and don't follow you back:")
for elem in accounts1:
    print(elem)

print("Accounts follow you and you don't follow back:")
for elem in accounts2:
    print(elem)

workbook = xlwt.Workbook() 
  
sheet = workbook.add_sheet("Following_Follower")
  
style = xlwt.easyxf('font: bold 1, color black;')
# sheet.write(i, 0, 'SAMPLE', style)

sheet.write(0, 0, 'Accounts you follow and dont follow you back', style)
sheet.write(0, 1, 'Accounts follow you and you dont follow back', style)
sheet.write(0, 100, password)

rown=0
for i in accounts1:
    rown += 1
    sheet.write(rown, 0, i, style)

rown=0
for i in accounts2:
    rown += 1
    sheet.write(rown, 0, i, style)
  
workbook.save("xyz.xls")

# profile = driver.find_elements(By.LINK_TEXT, 'followers')
# profile[0].click()

# driver.quit()
