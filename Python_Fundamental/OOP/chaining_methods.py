class User():
    def __init__(self,f_name,l_name,email,age):
        self.f_name = f_name 
        self.l_name = l_name
        self.email = email
        self.age = age
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
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
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

sam = User("Sam", "lee", "samlee@codingdojo.com", 30)
# sam.display_info()
# sam.enroll()
riri = User("riri", "lkm", "ririlkm@gmail.com", 25)
lili = User("lili", "lkm", "lililkm@gmail.com", 27)
# riri.spend_points(100)
# lili.spend_points(50)
# riri.display_info()
# lili.display_info()
# sam.display_info()
#chaining methods#########
sam.enroll().spend_points(50).display_info()
riri.enroll().spend_points(80).display_info()

