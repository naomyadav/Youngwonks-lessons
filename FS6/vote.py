# print('Q4')
#
#  age=int(input('Age?'))
# alist = [5, -2, 3,bool('True'),True]
# print(alist)
# if age >= 18:
#     Vote=input('Do you have a vote id? ').lower()
#     if (Vote == 'yes') or (Vote == 'true'):
#         print('Hurray, you are eligible to vote and you have a voter id card so you can vote.')
#     elif Vote == 'no' or Vote == 'false':
#         print("Sorry, you are eligible to vote but cannot vote since you don't have a voter id card")
#     else:
#         print("ERORR:not(input == no,yes,false,true)")
# else:
#     print('You are not eligible to vote')

# print('Q2')
#
# day = input('What is the day of the week\n').lower()
# if day in ['wednesday', 'wed','3','3rd','Sale Day']:
#     which=input('Which Wednesday of the month is it?\n').lower()
#     if which in ['2nd','second','2']:
#         print('Yay! Lets go shoping!\n')
#     else:
#          print('There is no sale today\n')
# else:
#      print('There is no sale today\n')


user_number = int(input('Ask the user to enter a number: '))

if user_number % 2 == 0:
    print('Divisible by 2')
    if user_number % 4 == 0:
        print('Multiple of 4') 
    else:
        print('Not a multiple of 4')
else:
    if user_number % 3 == 0:
        print('Multiple by 3')
    else:
        print()