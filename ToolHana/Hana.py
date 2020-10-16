import argparse
import sys
from random import randint
from time import sleep

from selenium import webdriver

Hana_URL = "https://fb.vieclamonline.org/login"



def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))

def initDriver():
    filepath='chrome'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "user-data-dir=" + filepath)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
class HanaLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = initDriver()

    def login(self):
        self.driver.get(Hana_URL)
        username_ele = self.driver.find_element_by_css_selector('#username')
        username_ele.send_keys(self.username)
        random_sleep(1, 5)
        password_ele = self.driver.find_element_by_css_selector('#password')
        password_ele.send_keys(self.password)
        random_sleep(1, 5)
        login_ele = self.driver.find_element_by_css_selector('#inspire > div > main > div > div > div > div.col-sm-8.col-md-6.col-lg-4.col-xl-4.col-12 > div > div.v-card__text > div > button > span')
        random_sleep(1, 5)
        login_ele.click()

hana = HanaLogin('vanquyetc2vc1','quyetdaica123')
hana.login()
