def LuuFile(path):
    n=int(input('Nhap so luong:'))
    file=open(path,'a',encoding='utf-8')
    for i in range(n):
        a=input('Nhap ma:')
        b=input('Nhap ten:')
        c=int(input('Nhap don gia:'))
        file.writelines("{0}\t{1}\t{2}\n".format(a,b,c))
    file.close()

LuuFile('QLSP.txt')
