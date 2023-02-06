num1 = 42 C / data type primitive Numbers
num2 = 2.3 #- variable declaration
boolean = True #-variable declaration-Data Types-Primitive-Boolean
string = 'Hello World' #-variable declaration-string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration/list-initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#variable declaration/dictionary-initialize
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration/types-initialize
print(type(fruit))#log statement/type check
print(pizza_toppings[1])#log statement/list-acces value
pizza_toppings.append('Mushrooms')# - List -- add value
print(person['name'])#log statement-dictionary-access value
person['name'] = 'George'#- Dictionary- change value
person['eye_color'] = 'blue'#- Dictionary/ - add value
print(fruit[2])#log statement/- Tuples - access value

if num1 > 45:#- if
    print("It's greater")#log statement
else:#- conditional-else
    print("It's lower")#log statement

if len(string) < 5:#- conditional-if
    print("It's a short word!")#log statement
elif len(string) > 15:#- conditional-elif
    print("It's a long word!")#log statement
else:#- conditional-else
    print("Just right!")#log statement

for x in range(5):#- for loop/start from 0 /stoped in 4
    print(x)#- log statement x



for x in range(2,5):#- for loop/start from 2 /stoped in 5
    print(x)#- log statement x
for x in range(2,10,3):#for loop / start from 2 /stoped in 10 / increment with 3
    print(x)#- log statement x   

x = 0#variable declaration-initialize /numbers
while(x < 5):#- while loop/start fom 0 ,stoped in 4
    print(x)#log statement
    x += 1#- increment by 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:# conditional/ for loop
    if topping == 'Pepperoni':
        continue #- continue
    print('After 1st if statement')
    if topping == 'Olives':
        break#break

def print_hello_ten_times():#function/
    for num in range(10):#conditional/ for loop start from 0 stoped in 9
        print('Hello')#log statement

print_hello_ten_times()

def print_hello_x_times(x):#function/parameter
    for num in range(x):# for loop
        print('Hello')#log statement


print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10)#function/argument
    for num in range(x):# for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)