nums=[i for i in range(1000,10000,1) if i%45==0]
print(nums)
evsq=[i**2 for i in range(100) if i%2==0]
total=0
for i in range(len(evsq)):
    total=total+evsq[i]
print(total)
fib=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(13):
    for n in range(i-1):
        print(fib[n],end="")
    print()
    
nums2=[1,2,3,4,5,6,7,8,9]
N = 9
for i in range(N):
    for n in range(i+1):
        print(nums2[i],end="")
    print()
    
nums2=[8,7,6,5,4,3,2,1]
for i in range(8):
    for n in range(nums2[i]):
        print(nums2[i],end="")
    print()