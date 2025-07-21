from time import sleep
list1=[]
for i in range(1,101,1):
    print(i)
    list1.append(i)
for i in range(len(list1)):
    print(list1[i],end="")
    

for i in range(155):
    for n in range(i):
        print("*",end="")
    print()
for i in range(155,0,-1):
    for n in range(i):
        print(" ",end="*")
    print()
    
t=2
for i in range(1,5):
    for n in range(i):
        print(chr(47+t),end="")
        t+=1
    print()