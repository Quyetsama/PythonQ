
s=input('Nhap mot chuoi:')
def InHoa(s):
    count=0
    for i in range(0,len(s)):
        if s[i].isupper():
            count+=1
    print('Co',count,'chu in hoa!')


def ChuSo(s):
    count=0
    for i in range(0,len(s)):
        if s[i].isnumeric():
            count+=1
    print('Co',count,'chu so!')
InHoa(s)
ChuSo(s)