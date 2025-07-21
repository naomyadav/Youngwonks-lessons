grades=[[50,70],[50,90],[40,70]]
sum1=0
for i in grades:
    sum1+=i[1]
    print(i)
sum1=sum1//len(grades)
print(sum1)