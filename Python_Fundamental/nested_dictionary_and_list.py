#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

students = [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# sports_directory['soccer'][0] = 'Andres'
# print( sports_directory['soccer'])


# students[0]['last_name'] = "bryant"
# print(studens)

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def iterate_dictionary(rihab):
#     for i in range(0, len(rihab)):
#         output = ""
#         for key,val in rihab[i].items():
#             output += f" {key} - {val},"
#         print(output)

# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         print(some_list[i][key_name])

# iterateDictionary2('last_name', students)
def printInfo(some_dict):
    
    for key,val in some_dict.items():
        print(len(val),key.upper())
        for i in range(0,len(val)):
            print(val[i])
        print('/////////////////////////////////')        
printInfo(dojo)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
