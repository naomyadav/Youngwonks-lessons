


class Bank:
    def __init__(self, name, account_num, total_balance):
        self.name = name
        self.account_num = account_num
        self.total_balance = total_balance


    def show(self):
        s = f"Name: {self.name} | Account Number: {self.account_num} | Total Balance: {self.total_balance}".format(self.name, self.account_num, self.total_balance)
        print(s)
    
    def transfer(self, transfer, user):
        self.total_balance-=transfer
        exec(f"{user.total_balance}={user}.total_balance+{transfer}")
    def deposit_func(self, deposit):
        self.total_balance = self.total_balance+deposit

    def withdraw_func(self, withdrawal):
        self.total_balance = self.total_balance-withdrawal
    
    def help(self):
        print("Help:\n/info Show your information\n/withdraw Witdraw Money\n/deposit Deposit Money\n/transfer Transfer Moneu\n/help Open This Menu")
    

i = input("Welcome Please Type any enter to start or type f then enter to add friends")
if i == "f":
    f = int(input("How many friends Would You Like To Add?"))
    for i in range(f):
        exec(f"friend{i}=Bank(10,{input(f"What is your {i}th friend's Name?")},80)")


Name=input("Name: ")
person1 = Bank(Name, id(Name), 80)
person1.show()


print(Name+"'s Bank Account Terminal")
person1.help()
while True:
    command=input(Name+"% ")
    if command == "/help":
        person1.help()
    elif command=="/info":
        person1.show()
    elif command=="/deposit":
        person1.deposit_func(int(input("Deposit:  ")))
    elif command=="/withdraw":
        person1.withdraw_func(int(input("Withdraw:  ")))
    elif command=="/transfer":
        person1.transfer(int(input("Transfer:    ")),input("Name:   "))
    else:
        print("InputError: Invalid Input")