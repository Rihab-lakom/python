from bank_account import BankAccount
class User():
    allUsers = []
    def __init__(self,f_name,l_name,email,age):
        self.f_name = f_name 
        self.l_name = l_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate=0.02, balance=0)
        # the status is set to True by default
        self.is_rewards_member = False
        self.gold_card_points =0
        
# Methods:
    # display_info(self) - Have this method print all 
    # of the users' details on separate lines.

    def display_info(self):
        print(f"F name: {self.f_name}")
        print(f"l name: {self.l_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        # print(f"Member: {self.is_rewards_member}")
        # print(f"Current Points: {self.gold_card_points}")
        return self

#enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
# spend_points(self, amount) - have this method decrease
#  the user's points by the amount specified.
    def spend_points(self ,amount):
        self.gold_card_points -= amount
        return self
#Add a make_deposit method to
#  the User class that calls on it's bank account's instance methods
    def make_deposit(self, amount):
        print(self.account.deposit(amount))

#Add a make_withdrawal method to the User class that calls on it's
#  bank account's instance methods
    def make_withdraw(self,amount):
        print(self.account.withdraw(amount))
#Add a display_user_balance method to the User class that displays user's account balance

    def display_user_balance(self):
        print(self.account.display_account_info())

sam = User("Sam", "lee", "samlee@codingdojo.com", 30)
# sam.display_info()
# sam.enroll()
# riri = User("riri", "lkm", "ririlkm@gmail.com", 25)
# lili = User("lili", "lkm", "lililkm@gmail.com", 27)
# riri.spend_points(100)
# lili.spend_points(50)
# riri.display_info()
# lili.display_info()
# sam.display_info()
# #chaining methods#########
# sam.enroll().spend_points(50).display_info()
# riri.enroll().spend_points(80).display_info()
sam.make_deposit(50)
# riri.make_withdraw(100)
sam.display_user_balance()