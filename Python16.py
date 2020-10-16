s='''Quyet Van Nguyen
lop 12c2
ahihihi'''
c=' '
x=s.splitlines()
for i in x:
    c=c+i
    print(i)
print(c)
s1='-'
s2=s1.join(x)
print(s2)
print(int(len(s)))