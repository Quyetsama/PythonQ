for i in range(1,10):
    for j in range(2,10):
        print("{0}*{1}={2:>2}".format(j,i,i*j),end="     ")
    print()