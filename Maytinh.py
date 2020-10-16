from tkinter import *
from Makecenterlib import *

def Cong():
    x = float(hesoa.get())
    y = float(hesob.get())
    ketquac.set(x+y)
def Tru():
    x = float(hesoa.get())
    y = float(hesob.get())
    ketquac.set(x-y)
def Nhan():
    x = float(hesoa.get())
    y = float(hesob.get())
    ketquac.set(x*y)
def Chia():
    x = float(hesoa.get())
    y = float(hesob.get())
    ketquac.set(x/y)
def AC():
    hesoa.set('')
    hesob.set('')
    ketquac.set('')
root=Tk()
hesoa=Variable()
hesob=Variable()
ketquac=Variable()
root.title('May tinh')
root.resizable(height=True,width=True)
root.minsize(height=300,width=300)
Label(root,text='Cộng trừ nhân chia',fg='red',font=('tohama',16),justify=CENTER).grid(row=0,columnspan=3)

a=Frame()
b=Frame()
Button(a,text='Cộng',command=Cong).pack(side=TOP,fill=X)
Button(a,text='  Trừ  ',command=Tru).pack(side=TOP,fill=X)
Button(a,text='Nhân',command=Nhan).pack(side=TOP,fill=X)
Button(a,text=' Chia ',command=Chia).pack(side=TOP,fill=X)
Button(b,text=' Thoát ',command=quit).pack(side=RIGHT)
Button(a,text=' AC ',command=AC).pack(side=TOP,fill=X)
a.grid(row=1,column=0,rowspan=4)
b.grid(row=4,column=2)

Label(root,text='Số a:').grid(row=1,column=1)
Entry(root,width=30,textvariable=hesoa).grid(row=1,column=2)
Label(root,text='Số b:').grid(row=2,column=1)
Entry(root,width=30,textvariable=hesob).grid(row=2,column=2)
Label(root,text='Kết quả:').grid(row=3,column=1)
Entry(root,width=30,textvariable=ketquac).grid(row=3,column=2)






makecenter(root)
root.mainloop()