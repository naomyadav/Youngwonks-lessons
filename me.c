class Bank:
    def __init__(self, name, account_num, total_balance):
        self.name = name
        self.account_num = account_num
        self.total_balance = total_balance


    def show(self):
        s = "Name: {} | Account Number: {} | Total Balance: {}".format(self.name, self.account_num, self.total_balance)
        print(s)

    def deposit_func(self, deposit):
        self.total_balance = self.total_balance+deposit

    def withdraw_func(self, withdrawal):
        self.total_balance = self.total_balance-withdrawal



person1 = Bank("Molly", 98765, 80)
person1.show()



print("Would you like to deposit money?")
deposit = input()
if deposit == "Yes":
    print("How much money would you like to deposit?")
    deposit_money = int(input())
    person1.deposit_func(deposit_money)
elif deposit == "No":
    print("Okay.")



print("Would you like to withdraw money?")
withdraw = input()
if withdraw == "Yes":
    withdraw_money = int(input())
    print("How much money would you like to withdraw?")
    person1.widthdraw_func(withdraw_money)
elif deposit == "No":
    print("Okay.")