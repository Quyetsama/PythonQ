def dequy(n):
    if n==1:
        return 1
    else:
        return n*dequy(n-1)
n=int(input('Nhap n:'))
kq=dequy(n)
print(kq)