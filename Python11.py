from math import sqrt
#quyet
n=int(input('Nhap n:'))
s=0
for i in range(1,n+1):
    s=sqrt(2+s)
print(s)