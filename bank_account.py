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

Acc1=BankAccount(0.01,100)
Acc1.deposit(100).deposit(50).deposit(30).withdraw(20).yield_interest().display_account_info()

Acc2=BankAccount(0.01,0)
Acc2.deposit(500).deposit(500).withdraw(50).withdraw(150).withdraw(50).withdraw(250).yield_interest().yield_interest()


