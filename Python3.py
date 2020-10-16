d=int(input("Nhap ngay"))
m=int(input("Nhap thang"))
y=int(input("Nhap nam"))
if m in (1,3,5,7,8,10):
    if d==31:
        print(1, "/", m+1, "/", y)
    else:
        print(d+1, "/", m, "/", y)
elif m==12 and d==31:
    print("1/ 1/", y+1)
else:
    print(d+1, "/", m, "/", y)

