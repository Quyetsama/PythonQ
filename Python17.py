def KiemTra(s):
    for i in range(0,int(len(s))//2):
        if(s[i]!=s[len(s)-1]):
            return False
        else:
            return True
while True:
    s=input("Nhap 1 Chuoi:")
    if KiemTra(s):
        print('La Chuoi Doi Xung!')
    else:
        print('Khong Phai Chuoi Doi Xung!')
    hoi=input('Ban co muon nhap tiep?c/k:')
    if hoi=='k':
        break
print('Bye!')