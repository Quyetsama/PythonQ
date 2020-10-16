
# S(n) =x + x^3/3! + x^5/5! + … + x^(2n+1)/(2n+1)!


x=int(input("Nhap x:"))
n=int(input("Nhap n:"))
s=x
m=mau=1
i=j=1
for i in range(1,n+1):
    tu=x**(2*i+1)
    m=2*i+1
    mau=mau*m*(m-1)
    s=s+(tu/mau)
print(s)
