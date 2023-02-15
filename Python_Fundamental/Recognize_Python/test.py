# riri = []
# def count_dawn (x):
#     for i in range (x,-1,-1):
#         riri.append(i)
        
#     return riri
# count_dawn(50)
# print(riri)


class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
    	# the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# 