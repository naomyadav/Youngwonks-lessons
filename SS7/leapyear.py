year=input('what year is it ?')
year=int(year)
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('leap year')
        else:
            print('normal year')
    else:
        print('leap year')
else:
    print('normal year')