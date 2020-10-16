# def printPetNames(owner, **pets):
#     print(f"Owner Name: {owner}")
#     for pet,name in pets.items():
#        print(f"{pet}: {name}")
#     a=pets
#     print(a)
#     for i in a:
#         for j in i:
#             print(j)
# printPetNames("Jonathan", c="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")


# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
#
# date2 = Date.from_string('11-09-2012')
# print(date2.__dict__)
# is_date = Date.is_date_valid('11-09-2012')

# class Employee:
#     empcount=0
#     st=0
#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary
#         self.st=Employee.empcount
#         Employee.empcount+=1
#     def stt(self):
#         print('total employee %d'%Employee.empcount)
# linh=Employee('linh',1000)
# thang=Employee('thang',999)
# print(linh.st)
# print(thang.st)
#

                                    # regex
# import re
# regexl=re.compile(r'Xin(.*?)moi')
# chuoi='Xin chao moi nguoi'
# kq=regexl.search(chuoi)
# kq.group()
# print(kq.group(1))
#
#
# ndung='''xin chao moi nguoi minh ten la python nay
# minh cung ten la python nay'''
# regex1=re.compile(r'ten (.*?) nay')
# final=regex1.findall(ndung)
# print(final)

import os
from shutil import copyfile
import io
# lay duong dan hien tai
# print(os.getcwd())

# doi duong dan file
# os.chdir(r'E:\baitap\[EAZY DESIGN] Neon Style')

# tao file
# file=open('quyetsama.txt','w')
# file.close()

# doi ten file
# os.rename('quyetsama.txt','quyetdaica.txt')

# copyfile
# copyfile('quyetdaica.txt','quyetsama.txt')


# tenfile='quyetsama.txt'
# file=open(tenfile,'a',encoding='utf-8')
# nd='Nguyễn Văn Quyết'
# file.write(nd+'\n')
# file.close()

# docfile
# file=io.open('quyetsama.txt','r',encoding='utf-8')
# list_lines=file.readlines()
# print(list_lines)
# for line in list_lines:
#     print(line)

# tuong tac voi file excel
import openpyxl


def get_value_excel(filename,cellname):
    wb=openpyxl.load_workbook(filename)
    Sheet1=wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value

def update_value_excel(filename,cellname,value):
    wb=openpyxl.load_workbook(filename)
    Sheet1=wb['Sheet1']
    Sheet1[cellname].value=value
    wb.close()
    wb.save(filename)

# filename='file.xlsx.xlsx'
# cellname='C5'
# value='van'
# bienx=get_value_excel(filename,cellname)
# update_value_excel(filename,cellname,value)
# print('bienx',bienx)

accou='C'
passw='D'
filename='file.xlsx.xlsx'

for i in range(5,20):
    cellacc='{}{}'.format(accou,i)
    cellpass='{}{}'.format(passw,i)
    account=get_value_excel(filename, cellacc)
    password=get_value_excel(filename, cellpass)
    print(account)
    print(password)
    input('______________')
