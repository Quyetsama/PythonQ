n=int(input('Nhap n:'))
m=int(input('Nhap m:'))
c=[]
def Nhap(n,m):
    for i in range(n):
        onec=[]
        for j in range(m):
            print('Nhap gia tri:')
            onec.append(int(input()))
        c.append(onec)
# def Xuat(n,m):
#     for x in range(len(c)):
#         for y in range(len(c[x])):
#             print(c[x][y],end=' ')
#         print()
def Xuat(n,m):
    for i in range(n):
        for j in range(m):
            print(c[i][j],end='\t')
        print()
def XuatDong(n,m):
    k=int(input('Nhap dong muon xuat:'))
    for i in range(m):
        print(c[k-1][i],end=' ')
    print()
def XuatHang(n,m):
    k=int(input('Nhap cot muon xuat:'))
    for i in range(n):
        print(c[i][k-1])



Nhap(n,m)
Xuat(n,m)
XuatDong(n,m)
XuatHang(n,m)