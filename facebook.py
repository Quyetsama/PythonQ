# from selenium import webdriver
# from time import sleep
#
#
# class HelloSelenium:
#     def __init__(self, url):
#         self.driver = webdriver.Chrome()
#         self.driver.get(url)
#
#     def get_site_info(self):
#         print('URL:', self.driver.current_url)
#         print('Title:', self.driver.title)
#         sleep(5)
#         self.driver.save_screenshot('screen_shot.png')
#
#
# if __name__ == '__main__':
#     hello = HelloSelenium('https://www.facebook.com/Quyetsama28/')
#     hello.get_site_info()
#     # Close driver
#     hello.driver.close()
import argparse
import sys
from random import randint
from time import sleep

from selenium import webdriver

FB_URL = "https://mbasic.facebook.com"
LinkPost = "https://mbasic.facebook.com/jazzapplevn/?_rdr"

def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


class FacebookLogin:
    def __init__(self, username, password, word):
        self.username = username
        self.password = password
        self.word= word
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(FB_URL)
        username_ele = self.driver.find_element_by_css_selector('#m_login_email')
        username_ele.send_keys(self.username)
        random_sleep(1, 5)
        password_ele = self.driver.find_element_by_css_selector('#login_form > ul > li:nth-child(2) > section > input')
        password_ele.send_keys(self.password)
        random_sleep(1, 5)
        login_ele = self.driver.find_element_by_css_selector('#login_form > ul > li:nth-child(3) > input')
        random_sleep(1, 5)
        login_ele.click()
        # random_sleep(1, 5)
        # self.driver.get(LinkPost)
        # like_ele = self.driver.find_element_by_css_selector('#sub_profile_pic_content > div > div.cq > table > tbody > tr > td:nth-child(1) > a')
        # random_sleep(1, 5)              like page
        # like_ele.click()
        # click_ele= self.driver.find_element_by_css_selector('#js_3 > div > div > div._2t-e > div:nth-child(1) > h1 > a > span')
        # random_sleep(5, 10)             load lai newfeed
        # click_ele.click()
        self.driver.get(FB_URL)
        word_ele= self.driver.find_element_by_css_selector('#mbasic-composer-form > table > tbody > tr > td.t > div > textarea')
        word_ele.send_keys(self.word)
        random_sleep(1, 5)
        post_ele = self.driver.find_element_by_css_selector('#mbasic-composer-form > table > tbody > tr > td:nth-child(3) > div > input')
        random_sleep(1, 5)
        post_ele.click()
    # def verify_login(self):
    #     try:
    #         self.driver.find_element_by_css_selector('#email')
    #         return False
    #     except:
    #         return True
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default=None, required=True)
    parser.add_argument('--password', default=None, required=True)
    parser.add_argument('--word', default=None, required=True)


    options = parser.parse_args()


    fb = FacebookLogin(options.username, options.password, options.word)
    fb.login()
    # if fb.verify_login():
    #     print('Đăng nhập thành công!')
    # else:
    #     print('Đăng nhập thất bại')
