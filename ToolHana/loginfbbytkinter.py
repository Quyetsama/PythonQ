# from loginfb import *
from test import *
from tkinter import *
from Makecenterlib import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from multiprocessing import Pool
import time
from time import sleep
def Quit():
    pass
def ham_surf_face(filePath):
    driver = initDriver(filePath)
    driver.get('https://mbasic.facebook.com')
    sleep(3)
    driver.get('https://fb.vieclamonline.org')
    sleep(5)
    kiemtien = driver.find_element(By.XPATH, './/*[@id="app"]/div/div[1]/nav/div[1]/div[2]/div[2]/a[2]/div[2]')
    kiemtien.click()
    sleep(1)
    kiemtienngay = driver.find_element(By.XPATH, './/*[@id="app"]/div/main/div/div/div[1]/div[1]/div[3]/a/span')
    kiemtienngay.click()
def pool_handler():
    p = Pool(4)
    kq = p.map_async(ham_surf_face, ('chrome1', 'chrome2'))

def tkin():
    root=Tk()
    stringProfile=StringVar()
    # stringMk=StringVar()
    root.title('Auto Hana')
    root.resizable(height=True,width=True )
    root.minsize(height= 400,width= 350)
    Label(root,text='Auto Qsama',fg='blue',font=('toahama',16),justify=CENTER).grid(row=0,columnspan=2)
    listbox=Listbox(root,width=58)      #listbox phải khai báo 2 dòng
    listbox.grid(row=1,columnspan=2)
    Label(root,text='Profile:').grid(row=2,column=0)
    Entry(root,width=43,textvariable=stringProfile).grid(row=2,column=1)
    # Label(root,text='Mật khẩu:').grid(row=3,column=0)
    # Entry(root,width=43,textvariable=stringMk).grid(row=3,column=1)

    e=Frame()
    Button(e,text='Bắt đầu',command=pool_handler).pack(side=LEFT)
    e.grid(row=5,column=0)
    Button(e,text='Kết thúc',command=Quit).pack(side=LEFT)
    e.grid(row=5,column=1)

    makecenter(root)
    root.mainloop()

if __name__ == '__main__':
    tkin()
    pool_handler()
