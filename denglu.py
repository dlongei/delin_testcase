import re
import requests
import pytesseract
from selenium import webdriver
from PIL import Image, ImageEnhance
import time
import unittest

driver = webdriver.Chrome()
driver.get('http://192.168.3.37:8001/')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//*[@id="username"]').send_keys('nifei')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('88861777')
time.sleep(1)
while True:
    driver.find_element_by_xpath('//*[@id="verifycode"]').clear()   #清空验证码输入框
    screenImg = 'E:\p\screenImg.png'    # 截图或验证码图片保存地址
    driver.get_screenshot_as_file(screenImg)    # 浏览器页面截屏
    time.sleep(2)
    # 定位验证码位置及大小
    location = driver.find_element_by_xpath('//*[@id="login_verifycode"]').location
    size = driver.find_element_by_xpath('//*[@id="login_verifycode"]').size
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    img = Image.open(screenImg).crop((left, top, right, bottom))
    time.sleep(2)
    # 图片处理
    img = img.convert('RGBA')
    img = img.convert('L')
    img = ImageEnhance.Contrast(img)
    img = img.enhance(2.0)
    img.save(screenImg)
    time.sleep(2)
    # 识别验证码
    img = Image.open(screenImg)
    code = pytesseract.image_to_string(img)
    time.sleep(2)
    # 去特殊符号
    b = ''
    for i in code.strip():
        pattern = re.compile(r'[a-zA-Z0-9]')
        m = pattern.search(i)
        if m != None:
            b += i
    time.sleep(2)
    print(b)
    # 输入验证码，提交
    driver.find_element_by_xpath('//*[@id="verifycode"]').send_keys(b)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="btnlogin"]').click()
    time.sleep(5)

    # 验证是否登录进系统首页,若未登陆，继续识别验证码
    if driver.current_url == 'http://192.168.3.37:8001/Home/AdminLTE':
        print('登录成功！')
        break



    '''
    # 获取cookie，并把cookie转化为字符串格式
    cookie1 = str(driver.get_cookies())
    print(cookie1)

    # 看cookie里是否有tokenId这个词，如果有说明登录成功，跳出循环
    # 如果没有，则表示登录失败，继续识别验证码
    match0bj = re.search(r'tokenId', cookie1, re.M | re.I)
    if match0bj:
        print(match0bj.group())
        break
    else:
        driver.find_element_by_xpath('//*[@id="login_verifycode"]').click()
    '''