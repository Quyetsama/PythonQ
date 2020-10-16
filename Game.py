while True:
    count = 0
    while True:
        from random import randrange
        x = randrange(1, 100)
        print(x)
        y = int(input('Nhập một số:'))
        print('Số của bạn lớn hơn hay nhỏ hơn số của máy?l/n:', end='')
        hoi = input()
        if ((y > x) and (hoi == 'l')) or ((y < x) and (hoi == 'n')):
            print('You Win!')
            break
        if ((y > x) and (hoi == 'n')) or ((y < x) and (hoi == 'l')):
            count += 1
            if count<3:
                z = 3 - count
                print('Sai rồi bạn vẫn còn', z, 'cơ hội')
        if count == 3:
            print('You lost!')
            break
    hoi1 = input('Bạn có muốn tiếp tục?c/k:')
    if hoi1=='k':
        break
print('Bye!')