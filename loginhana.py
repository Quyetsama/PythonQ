from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from random import randint
import time


'''đăng nhập 1 tk'''
driver=webdriver.Chrome()
driver.get('https://fb.vieclamonline.org/login')
tkelement=driver.find_element(By.XPATH,'.//*[@id="username"]')
tkelement.send_keys('quyetsama')
time.sleep(5)
passelement=driver.find_element(By.XPATH,'.//*[@id="password"]')
passelement.send_keys('quyetdaica123')
time.sleep(5)
elem=driver.find_element(By.XPATH,'.//*[@id="inspire"]/div/main/div/div/div/div[1]/div/div[2]/div/button/span')
elem.click()
time.sleep(5)
kiemtien=driver.find_element(By.XPATH,'.//*[@id="app"]/div/div[1]/nav/div[1]/div[2]/div[2]/a[2]/div[2]')
kiemtien.click()
time.sleep(2)
kiemtienngay=driver.find_element(By.XPATH,'.//*[@id="app"]/div/main/div/div/div[1]/div[1]/div[3]/a/span')
kiemtienngay.click()
time.sleep(60)
jobfl=driver.find_element(By.XPATH,'.//*[@id="app"]/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/a/div/div[1]/div/div/img')
jobfl.click()