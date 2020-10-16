from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from random import randint
from multiprocessing import Pool

'''đăng nhập 1 tk'''
# driver=webdriver.Chrome()
# driver.get('https://mbasic.facebook.com/')
# tkelement=driver.find_element(By.XPATH,'.//*[@id="m_login_email"]')
# tkelement.send_keys('dieppham754593@hogee.com')
# time.sleep(5)
# passelement=driver.find_element(By.XPATH,'.//*[@id="login_form"]/ul/li[2]/section/input')
# passelement.send_keys('quyetdaica123@')
# time.sleep(5)
# elem=driver.find_element(By.XPATH,'.//*[@id="login_form"]/ul/li[3]/input')
# elem.click()
# time.sleep(10)
#
# driver.get('https://mbasic.facebook.com/NguyenKimChi.Official/')
# time.sleep(3)
# likeelem=driver.find_element(By.XPATH,'.//*[@id="sub_profile_pic_content"]/div/div[2]/table/tbody/tr/td[1]/a')
# likeelem.click()



'''đăng nhâp nhiều tk'''
FB_URL = "https://mbasic.facebook.com"
LinkPost = "https://mbasic.facebook.com/jazzapplevn/?_rdr"

def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))

# khong load hinh anh chrome
def Kloadanh():
    chrome_optionss = webdriver.ChromeOptions()
    prefs = {
        "profile.managed_default_content_settings.images": 2
    }
    chrome_optionss.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_optionss)
    return driver
def initDriver():
    filepath='chrome2'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "user-data-dir=" + filepath)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

class FacebookLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = initDriver()
        # self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get(FB_URL)
        # self.driver.execute_script("window.open('','_blank');")             tab moi
        # tkelement = self.driver.find_element(By.XPATH, './/*[@id="m_login_email"]')
        # tkelement.send_keys(self.username)
        # random_sleep(1, 5)
        # passelement = self.driver.find_element(By.XPATH, './/*[@id="login_form"]/ul/li[2]/section/input')
        # passelement.send_keys(self.password)
        # random_sleep(1, 5)
        # elem = self.driver.find_element(By.XPATH, './/*[@id="login_form"]/ul/li[3]/input')
        # elem.click()
        # self.driver.get('https://mbasic.facebook.com/search/top/?q=kim+chi&refid=8&_rdr')
        # like =self.driver.find_element(By.XPATH, './/*[@id="BrowseResultsContainer"]/div[1]/div[1]/div/div/div/table/tbody/tr/td[3]/a/img')
        # like.click()
# def pool_handler():
#     p = Pool(2)
#     kq = p.map_async(FacebookLogin, ('chrome', 'chrome2'))
#     print('main')
#     print(kq.get())
#     p.close()
#     p.join()
#     print('Task ended. Pool join.')
# if __name__ == '__main__':
#     pool_handler()

profile1=FacebookLogin('dieppham754593@hogee.com','quyetdaica123@')
profile1.login()
profile2=FacebookLogin('bestkennenvn@gmail.com','quyetdaica')
profile2.login()
# //*[@id="BrowseResultsContainer"]/div[1]/div[1]/div/div/div/table/tbody/tr/td[3]/a/img
# //*[@id="BrowseResultsContainer"]/div[1]/div[2]/div/div/div/table/tbody/tr/td[3]/a/img
