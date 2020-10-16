import math
try:
    r=float(input("Nhập bán kính đường tròn:"))
    cv=2*math.pi*r
    dt=math.pi*r**2
    print("Chu vi dường tròn bán kính "+str(r)+" là:",cv)
    print("Diện tích đường tròn bán kính "+str(r)+" là:",dt)
except:
    print("Lỗi!")