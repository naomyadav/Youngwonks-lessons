a=0
t=0
n=5
l=0
# print("n=",n)
for i in range(n+1):
    # print("i=",i)
    l+=1
    
    print("row=",end=" ")
    for j in range(i+1):

        a+=1
        # print("j=",j)
        print(a,end=" ")
        
    print()

    t+=a
    # print("t=",t)
print(t)