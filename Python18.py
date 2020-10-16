s=input('Nhap 1 chuoi:')
s=s.strip()
def TachChuoi(s):
    arr=s.split()
    for i in arr:
        print(i)
    s1=' '
    s2=s1.join(arr)
    return s2
def InHoa(s):
    arr = s.split(" ")
    print(arr)
    for i in arr:

        for j in range(0, len(i)):
            if j == 0:
                print(i[0].upper(), end='')
            if j != 0:
                print(i[j], end='')
        print(end=' ')

x=TachChuoi(s)
print(x)
InHoa(x)
