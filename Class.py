class SieuNhan:
    sothutu=1
    def __init__(self,ten,vk,mausac):
        self.ten='Sieu nhan' + ten
        self.vk=vk
        self.mausac=mausac
        self.stt=SieuNhan.sothutu
        SieuNhan.sothutu+=1
    def __str__(self):
        return 'day la {}\nvk la {}\nmau sac la {}'.format(self.ten,self.vk,self.mausac)
    def __repr__(self):
        return 'day la {}\nvk la {}\nmau sac la{}'.format(self.ten, self.vk, self.mausac)
class SieuNhanQ(SieuNhan):
    def __init__(self,ten,vk,mausac,thu):
        super().__init__(ten,vk,mausac)
        self.thu=thu

sieunhanA= SieuNhanQ('quyet1','kiem1','do1','ngua1')
sieunhanb= SieuNhanQ('quyet2','kiem2','do2','ngua2')
print(sieunhanA.__dict__)
print(sieunhanb.__dict__)
print(sieunhanA.stt)
print(sieunhanb.stt)
print('%s'%sieunhanA)
print('%r'%sieunhanA)
