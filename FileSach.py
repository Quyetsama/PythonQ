path="QLSach.doc"
def LuuFile(line):
    try:
        file=open(path,'a',encoding='utf-8')
        file.writelines(line)
        file.writelines('\n')
        file.close()
    except:
        pass                                        #try với except không quan trọng
def DocFile():
    arrSach=[]
    try:
        file=open(path,'r',encoding='utf-8')
        for line in file:
            arr=line.strip().split(' ')
            arrSach.append(arr)
        file.close()
    except:
        pass
    return arrSach
s=DocFile()
def SapXep(s):
    for i in range(len(s)):
        for j in range(len(s)):
            a=s[i]
            b=s[j]
            if a[2]<b[2]:
                s[i]=b
                s[j]=a
def SuaFile():
    try:
        file=open(path,'w',encoding='utf-8')
        file.close()
    except:
        pass





