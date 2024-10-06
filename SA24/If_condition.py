
#Write a program to check if a person is eligible to drive. Ask the user to enter the age and store it into a variable. If the age is greater than or equal to 16 years, the program should print “You are eligible to drive”. If the person's age is under 16 years, the program should print “You are not eligible to drive”.
#18+ or not

age=int(input('how old are you?'))
if age>18:
    print('you are an adult')
elif age<18 and age>4:
    print('you are a kid')
elif age<4 and age >0:
    print('you are a babby')
elif age<0:
    print('invalid entry')