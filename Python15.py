

# https://toidicode.com/cac-ham-xu-ly-chuoi-trong-python-368.html


s='''Nguyen Van Quyet;lop12c2
Quyet Van Nguyen;lopc2
Van Quyet Nguyen;lop12
Quyet la tao'''
x=s.splitlines()
for i in  x:
    arr=i.split(';')
    if len(arr)==2:
        print(arr)