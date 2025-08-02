num = 5
start = 10
for i in range(5):
    for n in range(num):
        print(start-n,end=" ")
    print()
    start = start - 1
    num -= 1