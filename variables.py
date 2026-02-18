import sys
x=2
sys.set_int_max_str_digits(2147483647)
for error in range(0,10,1):
    x=((x**x)**x)**x
    print(x)