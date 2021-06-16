
class User:
    def __init__(self,nameOfUser, email):
        self.name=nameOfUser
        self.email=email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance +=amount

    def withdrow(self,amount):
        self.account_balance -= amount

    def transfer_fund(self,amount,other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
    
    def display_balance(self):
        print(f'{self.name} have a balance of {self.account_balance}')

user1=User("nkurunziza","nkurunziza@bank.com")
user2=User("kanye","kanye@bank.com")
user3=User("doe","doe@bank.com")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.withdrow(20)
user1.transfer_fund(40,user3)

user2.make_deposit(400)
user2.make_deposit(400)
user2.withdrow(150)
user2.withdrow(150)

user3.make_deposit(500)
user3.withdrow(50)
user3.withdrow(50)
user3.withdrow(50)


user1.display_balance()
user2.display_balance()
user3.display_balance()



