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
s=LuuFile('DaySo.txt')