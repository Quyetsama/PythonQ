from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#===cach click
driver.get('https://www.google.com.vn/?hl=vi')
#cach 1 : thuc thi js
# js_zzz="document.querySelector('.readmore').click()"
# driver.execute_script(js_zzz)

#cach 2: tim phan tu bang driver
# driver.find_element_by_css_selector('.readmore').click()
#trong truong hop nhieu phan tu thi dung find_elements_by_css_selector
# list_eles=driver.find_element_by_css_selector('.facebook')
#
# list_eles.click()