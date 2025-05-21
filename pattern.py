from mathHomeworkSolver import solveBasic
# # #Pattern
# # #1  1  1
# # #2  4  8
# # #3  9  27
# # #4 16  64
# # #.
# # #10 100 1000
N=10
for i in range(1,11,1):
    print(i,i**2,i**3)


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
print()
a=1
for i in range(1,6):
    for n in range(i):
        print(a,end=" ")
        a+=1
    print()

print()

a=""
N=10
for i in range(N+1):
    for n in range(N-i):
        print(" ",end="")
    for t in range(i):
        print(a,end=" ")
    print()

N=5
N2=N-1

for i in range(N):
    for n in range(N2):
        print(" ",end=" ")
    N2=N2-1
    for t in range(i+i-1):
        print("*",end=" ")
    print()


# solveBasic()