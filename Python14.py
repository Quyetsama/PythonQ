def Tong(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
n=int(input("Nhap n:"))
if Tong(n)==n:
    print('La so hoan hao!')
else:
    print('Khong phai la so hoan hao!')
if Tong(n) >n:
    print('La so thinh vuong!')
else:
    print('Khong phai la so thinh vuong!')