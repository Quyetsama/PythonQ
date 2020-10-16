from tkinter import *
from Makecenterlib import makecenter
def TiepAction():
    a.set('')
    b.set('')
    c.set('')
def GiaiPt():
    x = float(a.get())
    y = float(b.get())
    if x==0 and y==0:
        c.set('Vô số nghiệm')
    elif x==0 and y!=0:
        c.set('Vô nghiệm')
    else:
        c.set(-y/x)

root=Tk()
a=Variable()
b=Variable()
c=Variable()
root.title('Giải Pt')
root.resizable(height=True,width=True)
root.minsize(height=200,width=300)

Label(root,text='  Giải Phương Trình Bậc Nhất',fg='blue',font=('tohama',16),justify=CENTER).grid(row=0,columnspan=2)
# Button(root,text='Đăng Nhập',fg='red',command=root.quit).pack()
# e=StringVar()
# Entry(root,textvariable=e,width=30).pack()
Label(root,text='Hệ số a:').grid(row=1,column=0)
Entry(root,width=30,textvariable=a).grid(row=1,column=1)
Label(root,text='Hệ số b:').grid(row=2,column=0)
Entry(root,width=30,textvariable=b).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text='Kết Quả',command=GiaiPt).pack(side=LEFT)
Button(frameButton,text='Tiếp',command=TiepAction).pack(side=LEFT)
Button(frameButton,text='Thoát',command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)
Label(root,text='Kết quả:').grid(row=4,column=0)
Entry(root,width=30,textvariable=c).grid(row=4,column=1)
makecenter(root)
root.mainloop()