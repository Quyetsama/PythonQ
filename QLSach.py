from tkinter import *
from Makecenterlib import *
from FileSach import *

def Them():
    line=stringMa.get() +' '+ stringTen.get() +' '+ stringNam.get()
    LuuFile(line)
    stringMa.set('')
    stringTen.set('')
    stringNam.set('')
    ShowSach()          #Mỗi lần thêm thành công thì dữ liệu sẽ dc in ra listbox
def ShowSach():
    arrsach=DocFile()
    listbox.delete(0,END)   #xóa dữ liệu lúc đầu để khi thêm mới không bị in lặp lại
    for item in arrsach:
        listbox.insert(END,item)    #thêm dữ liệu vào cuối danh sách

def Sapxep():
    arrsach=DocFile()
    SapXep(arrsach)
    listbox.delete(0, END)
    for i in arrsach:
        listbox.insert(END,i)
def TimKiem():
    arrsach=DocFile()
    line=stringMa.get() + ' ' + stringTen.get() + ' ' + stringNam.get()
    listbox.delete(0, END)
    for i in arrsach:
        a=line.strip().split(' ')
        if i==a:
            listbox.insert(END, i)
            break
    else:
        listbox.insert(END, 'Không tìm thấy thông tin sách!')
def Menu():
    ShowSach()
def Xoa():
    arrsach=DocFile()
    arrsach1=[]
    s=' '
    line = stringMa.get() + ' ' + stringTen.get() + ' ' + stringNam.get()
    for i in arrsach:
        a=line.split(' ')
        s1=s.join(i)
        arrsach1.append(s1)
        if i==a:
            arrsach.remove(i)
    listbox.delete(0, END)
    for j in arrsach:
        listbox.insert(END, j)
    SuaFile()
    for k in arrsach1:
        LuuFile(k)
def Clear():
    listbox.delete(0, END)
    SuaFile()
root=Tk()
stringMa=StringVar()
stringTen=StringVar()
stringNam=StringVar()
root.title('Quản Lí Sách')
root.resizable(height=True,width=True )
root.minsize(height= 400,width= 350)
Label(root,text='Quản lý sách',fg='blue',font=('toahama',16),justify=CENTER).grid(row=0,columnspan=2)
listbox=Listbox(root,width=58)      #listbox phải khai báo 2 dòng
listbox.grid(row=1,columnspan=2)
ShowSach()
Label(root,text='Mã sách:').grid(row=2,column=0)
Entry(root,width=43,textvariable=stringMa).grid(row=2,column=1)
Label(root,text='Tên sách:').grid(row=3,column=0)
Entry(root,width=43,textvariable=stringTen).grid(row=3,column=1)
Label(root,text='Năm xuất bản:').grid(row=4,column=0)
Entry(root,width=43,textvariable=stringNam).grid(row=4,column=1)

e=Frame()
f=Frame()
Button(f,text='      Clear       ',command=Clear).pack(side=LEFT)
Button(e,text='Trang chính',command=Menu).pack(side=LEFT)
Button(e,text='Thêm',command=Them).pack(side=LEFT )
Button(e,text='Xóa',command=Xoa).pack(side=LEFT )
Button(e,text='Tìm',command=TimKiem).pack(side=LEFT)
Button(e,text='Sắp xếp',command=Sapxep).pack(side=LEFT)
Button(e,text='Thoát',command=quit).pack(side=LEFT)

e.grid(row=5,column=1)
f.grid(row=5,column=0)






makecenter(root)
root.mainloop()