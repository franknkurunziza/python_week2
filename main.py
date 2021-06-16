
class User:
    def __init__(self,nameOfUser, email):
        self.name=nameOfUser
        self.email=email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance +=amount
        return self

    def withdrow(self,amount):
        self.account_balance -= amount
        return self

    def transfer_fund(self,amount,other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    
    def display_balance(self):
        print(f'{self.name} have a balance of {self.account_balance}')

user1=User("nkurunziza","nkurunziza@bank.com")
user2=User("kanye","kanye@bank.com")
user3=User("doe","doe@bank.com")

user1.make_deposit(100).make_deposit(100).make_deposit(100).withdrow(20).transfer_fund(40,user3)

user2.make_deposit(400).make_deposit(400).withdrow(150).withdrow(150)

user3.make_deposit(500).withdrow(50).withdrow(50).withdrow(50)


user1.display_balance()
user2.display_balance()
user3.display_balance()



