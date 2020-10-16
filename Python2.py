t=int(input("Nhap thoi gian (s): "))

if t>9999:
    hour = ((t // 3600) % 24)-12
    minute = (t % 3600) // 60
    second = (t % 3600) % 60
    print("{0}:{1}:{2} PM".format(hour, minute, second))
else:
    hour = (t // 3600) % 24
    minute = (t % 3600) // 60
    second = (t % 3600) % 60
    print("{0}:{1}:{2} AM".format(hour, minute, second))














