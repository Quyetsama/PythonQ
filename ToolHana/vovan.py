import bs4
# import  requests
# import io
# response=requests.get('https://fb.vieclamonline.org/jobs/facebook/detail/96917')
# html_doc=response.text
# file=io.open('hana.html','w',encoding='utf-8')
# file.write(html_doc)
# import socket
#
#
# def print_machine_info():
#     host_name = socket.gethostname()
#     ip_address = socket.gethostbyname(host_name)
#     print("Host name: %s" % host_name)
#     print("IP address: %s" % ip_address)
#
#
# if __name__ == '__main__':
#     print_machine_info()
# a={"id":"001","name":"quyet1","cookies":"sb=001"}
# b={"id":"002","name":"quyet2","cookies":"sb=002"}
#
# print(a)
# print(len(a))
# print(a['id'])
# print(a.keys())
# print(a.values())
# print(a.items())
# y=[i[0] for i in a.items()]
# print(y)
# x=[i[1] for i in a.items()]
# print(x)
# c=dict(id='003', name='quyet3', cookies='sb=003')
# print(c)
# print(list(c))
# c['name']='quyetsama'
# print(c)
# print('name' in c)
# print('quyetsama' in c)
# # print(c.clear())
# print(c.pop('name'))
# print(c)


# def Sum(*data):
#     s=0
#     for i in data:
#         s=s+i
#     return s
# s=Sum(10,20,30)
# print(s)
#
# def Tong(*data):
#     list=[]
#     for i in data:
#         s=0
#         for j in i:
#             s=s+j
#         list.append(s)
#     return list
#
# s1=Tong([1,2,4,10],[20,30,10])
# print(s1)


# def TaiKhoan(**data):
#     for key,value in data.items():
#         json='{:20}{:10}'.format(key,value)
#         print(json)
#
# TaiKhoan(id='001',name='quyet',cookies='sb=kc')

# b = 'https://api.rentcode.net/api/v2/order/'
# c = '/check?apiKey=vivvTm7TgEYIJFV7I9tQvnvLsDtT9WQ8k51eeBPZAiQv'
# a = b+c
# print(a)





# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Firefox()
# driver.get('url')
#
# select = Select(driver.find_element_by_id('fruits01'))
#
# # select by visible text
# select.select_by_visible_text('Banana')
#
# # select by value
# select.select_by_value('1')



# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
#
#  # drop-down list selenium
# driver=webdriver.Chrome()
# driver.get('https://vi-vn.facebook.com/r.php')
# select1 = Select(driver.find_element_by_id('day'))
# select1.select_by_value('21')
# select2 = Select(driver.find_element_by_id('month'))
# select2.select_by_value('1')
# select3 = Select(driver.find_element_by_id('year'))
# select3.select_by_value('2001')

import bs4
import pandas
import requests

url = 'https://fb.vieclamonline.org/js/app.79cae9fe.js' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"en-US"})
   return bs4.BeautifulSoup(page.text,"html.parser")
soup = get_page_content(url)
print(soup)
# response = requests.get(url)
# x=response.json
# print(x)