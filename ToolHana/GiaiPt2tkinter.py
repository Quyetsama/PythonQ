from cmath import sqrt
from tkinter import *
from Makecenterlib import *
def Restart():
    hesoa.set('')
    hesob.set('')
    hesoc.set('')
def Giai():
    a=float(hesoa.get())
    b = float(hesob.get())
    c = float(hesoc.get())
    # d=b**2-(4*a*c)
    # x1=(-b-sqrt(d))/2*a
    # x2 = (-b + sqrt(d)) / 2 * a
    # if a==0 and b==0 and c==0:
    #     x.set('Vô số nghiệm!')
    # elif a==0 and b==0 and c!=0:
    #     x.set('Vô nghiệm!')
    # else:
    #     x.set('x={0}'.format(-c/b))
    # if a!=0:
    #     if d<0:
    #         x.set('Vô nghiêm!')
    #     elif d==0:
    #         x.set('x={0}'.format(-b/2*a))
    #     else:
    #         x.set('x1={0};x2={1}'.format(x1,x2))
    if a == 0:
        if b == 0:
            if c == 0:
                x.set('Vô số nghiệm!')
            else:
                x.set('Vô nghiệm!')
        else:
            x.set('x={0}'.format(-c/b))
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            x.set('Vô nghiệm!')
        elif delta == 0:
            x.set('x={0}'.format(-b/2*a))
        else:
            x.set('x1={0};x2={1}'.format((-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)))
root=Tk()
hesoa=Variable()
hesob=Variable()
hesoc=Variable()
x=Variable()
root.title('Giai Pt Bac2')
root.resizable(width=True,height=True)
root.minsize(width=400,height=300)

Label(root,text='Giải phương trình bậc 2',fg='red',font=('tohama',16),justify=CENTER).grid(row=0,columnspan=2)
Label(root,text='Hệ số a:',fg='blue').grid(row=1,column=0)
Entry(root,width=30,textvariable=hesoa).grid(row=1,column=1)

Label(root,text='Hệ số b:',fg='blue').grid(row=2,column=0)
Entry(root,width=30,textvariable=hesob).grid(row=2,column=1)

Label(root,text='Hệ số c:',fg='blue').grid(row=3,column=0)
Entry(root,width=30,textvariable=hesoc).grid(row=3,column=1)

e=Frame()
Button(e,text='Giải',command=Giai).pack(side=LEFT)
Button(e,text='Tiếp tục',command=Restart).pack(side=LEFT)
Button(e,text='Thoát',command=root.quit).pack(side=LEFT)
e.grid(row=4,columnspan=2)
Label(root,text='Kết quả:',fg='blue').grid(row=5,column=0)
Entry(root,width=30,textvariable=x).grid(row=5,column=1)


makecenter(root)
root.mainloop()
