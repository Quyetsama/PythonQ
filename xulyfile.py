def LuuFile(path):
    file=open(path,'w',encoding='utf-8')
    c=int(input('Nhap so dong:'))
    k=1
    arr2d=[]
    while k<=c:
        n=int(input('Nhap n:'))
        arr=[]
        for i in range(n):
            a = int(input())
            arr.append(a)
            if i!= n-1:
                file.writelines("{0},".format(a))
            else:
                file.writelines("{0}".format(a))
        # print(arr)
        arr2d.append(arr)
        file.writelines('\n')
        k+=1
    print(arr2d)
    file.close()
    return arr2d
def DocFile(path):
    file=open(path,'r',encoding='utf-8')
    for i in file:
        a=i.strip()
        print(a)
def XuatSoAm(s):
    print('So am tren moi dong!')
    for i in s:
        for j in i:
            if j<0:
                print(j,end='')
        print()



s=LuuFile('DaySo.txt')
DocFile('DaySo.txt')
XuatSoAm(s)


