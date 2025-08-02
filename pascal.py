for test in range(1,104):
    stars = test
    spaces = 4
    for i in range(4):
        spaces -= 1
        for n in range(spaces):
            print(" ",end="")
        for t in range(stars):
            print("*",end="")
        stars+=2
        print()