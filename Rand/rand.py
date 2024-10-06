from random import randint

num = randint (1,30)

if (num % 3 == 0) and (num % 2 == 0):
    print(num)
else:
    print('The number', num , ' is not divisible by 2 and 3.')