while True:
    n=int(input("Nhap n:"))
    count =0

    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("La so nto!")
    else:
        print("Khong phai so nto!")
    hoi=input("Ban co muon tiep tuc!c/k")
    if hoi is "k":
        break
print("Bye")