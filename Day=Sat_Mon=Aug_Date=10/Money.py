quarters=int(input('quarters = '))
dimes=int(input('dimes = '))
nickels=int(input('nickels = '))
pennies=int(input('pennies = '))
number_of_coins = quarters+dimes+nickels+pennies
print('Total number of coins are',number_of_coins)

#Find total in pennies
PENNIES_IN_QUARTER = 25
PENNIES_IN_DIME = 10
PENNIES_IN_NICKEL = 5
PENNIES_IN_PENNY = 1

tpiq = quarters * PENNIES_IN_QUARTER
tpid = dimes * PENNIES_IN_DIME
tpin = nickels * PENNIES_IN_NICKEL
tpip = pennies * PENNIES_IN_PENNY

total_sum_in_pennies = tpiq+tpid+tpin+tpip

print(total_sum_in_pennies)