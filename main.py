
class User:
    def __init__(self,nameOfUser, email):
        self.name=nameOfUser
        self.email=email
        self.bankaccounts=[]

    def another_acc(self,rate=0.02,balance=0):# default parameter
        self.bankaccounts.append(BankAccount(rate,balance))
        return self
    def made_deposit(self,amount,acc_number):
        self.bankaccounts[acc_number].deposit(amount)
        return self

    def make_withdraw(self,amount,acc_number):
        self.bankaccounts[acc_number].withdraw(amount)
        return self

    def display(self,acc_number):
        self.bankaccounts[acc_number].display_account_info()
        return self

    def display_all_account(self):
        for x in range(len(self.bankaccounts)):
            print(f'ACCOUNT #:{x}')
            self.bankaccounts[x].display_account_info()
        return self

class BankAccount:
    def __init__(self,int_rate,balance):
        self.rate=int_rate
        self.account_balance=balance
        
    def deposit(self,amount):
        self.account_balance +=amount
        return self

    def withdraw(self,amount):
        if self.account_balance>=amount:
            self.account_balance -=amount
        else:
            print("insufficient funds you will be charged $5")
            self.account_balance -=5
        return self

    def display_account_info(self):
        print(f'you have {self.account_balance} in your acoount')
        # return self

    def yield_interest(self):
        if self.account_balance>0:
            yield_amount=self.account_balance *self.rate
            self.account_balance+=yield_amount
        return self

user1=User("nkurunziza","nkurunziza@bank.com")
user2=User("kanye","kanye@bank.com")
user3=User("doe","doe@bank.com")

user1.another_acc(0.05,200).made_deposit(200,0)
user1.another_acc(0.04,300).another_acc(00.1,500).display_all_account()


