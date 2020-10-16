def DocFile(path):
    arrsp=[]
    file=open(path,'r',encoding='utf-8')
    for i in file:
        arr=i.strip().split('\t')
        arrsp.append(arr)
    file.close()
    return arrsp
dssp=DocFile('QLSP.txt')
# print(dssp[1])
# a=dssp[3]
# print(a[2])
def Xuat(dssp):
    for i in dssp:
        for j in i:
            print('{0:>10}'.format(j),end='')
        print()

def SapXep(dssp):
    for i in range(len(dssp)):
        for j in range(len(dssp)):
            a=dssp[i]
            b=dssp[j]
            if a[2]>b[2]:
                dssp[i]=b
                dssp[j]=a
# def GhiFile(path,dssp):
#
#     file=open(path,'a',encoding='utf-8')
#     for i in range(len(dssp)):
#         x=dssp[i]
#         file.writelines("{0}\t{1}\t{2}\n".format(x[0],x[1],x[2]))
#     file.close()

SapXep(dssp)
Xuat(dssp)
# GhiFile('QLSP.txt',dssp)






