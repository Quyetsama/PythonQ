
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from multiprocessing import Pool
import time
from time import sleep
# def Kloadanh():
#     chrome_optionss = webdriver.ChromeOptions()
#     prefs = {
#         "profile.managed_default_content_settings.images": 2
#     }
#     chrome_optionss.add_experimental_option("prefs", prefs)
#     driver = webdriver.Chrome(chrome_options=chrome_optionss)
#     return driver
# def initDriver(filePath):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(
#         "user-data-dir=" + filePath)
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     return driver
#
#
# def ham_surf_face(filePath):
#     driver = initDriver(filePath)
#     driver.get('https://mbasic.facebook.com')
#     sleep(3)
#     driver.get('https://fb.vieclamonline.org')
#     sleep(5)
#     kiemtien = driver.find_element(By.XPATH, './/*[@id="app"]/div/div[1]/nav/div[1]/div[2]/div[2]/a[2]/div[2]')
#     kiemtien.click()
#     sleep(1)
#     kiemtienngay = driver.find_element(By.XPATH, './/*[@id="app"]/div/main/div/div/div[1]/div[1]/div[3]/a/span')
#     kiemtienngay.click()
#
#
# def pool_handler():
#     p = Pool(2)
#     kq = p.map_async(ham_surf_face, ('chrome1', 'chrome2'))
#     print(kq.get())
#     # p.join()
# if __name__ == '__main__':
#     pool_handler()



import instaloader

x = instaloader -h