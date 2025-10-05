from tkinter import *
from tkinter import messagebox
def start_tkinter():
    root=Tk()
    root.title("Bank Browse")
    Label1=Label(root,text="Bank Browse Terminal\nCurently Logged in as an executive user")
    Label1.pack()
    Connect=Button(root,text="Connect",command=root.destroy)
    Connect.pack()
    Logout=Button(root,text="Log Out",command=lambda:print("Could Not Log Out"))
    Logout.pack()
    root.mainloop()
    print("Connected")
    
    
class Bank:
    def __init__(self, name, account_num, total_balance):
        self.name = name
        self.account_num = account_num
        self.total_balance = total_balance


    def show(self):
        s = f"Name: {self.name} | Account Number: {self.account_num} | Total Balance: {self.total_balance}".format(self.name, self.account_num, self.total_balance)
        print(s)

    def deposit_func(self, deposit):
        try:
            deposit=int(deposit)
            self.total_balance = self.total_balance+deposit
        except Exception as e:
            print(e)

    def withdraw_func(self, withdrawal):
        try:
            self.total_balance = self.total_balance-withdrawal
        except Exception as e:
            print(e)
    
    def help(self):
        print("Help:\n/info Show your information\n/withdraw Witdraw Money\n/deposit Deposit Money\n/help Open This Menu\n/disconnect Disconnects you from the online bank terminal")
    
    def disconnect(self):
        print("Disconnected")
        start_tkinter()

start_tkinter()
Name=input("Name: ")
person1 = Bank(Name, (Name), 80)
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
        person1.deposit_func(input("Deposit:  "))
    elif command=="/withdraw":
        person1.withdraw_func(int(input("Withdraw:  ")))
    elif command=="/disconnect":
        person1.disconnect()
    else:
        print("InputError: Invalid Input")