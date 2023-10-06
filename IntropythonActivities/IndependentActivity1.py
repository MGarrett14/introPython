# read and review the following pages on Python lists. Use these to help you solve
# the questions. 

linkOne= '# read and review the following pages on Python lists. Use these to help you solve'
# the questions. 

linkOne= 'https://www.w3schools.com/python/python_lists.asp'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.  

favorite_games =['genshin impact', 'madden', 'cookie run kingdom', '2k', 'honkai star rail',]

# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3
zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']

print(zoo_animals[3])

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']

print(sports_on_tv[0])

# find and print index 0
random_numbers = [10,100,12123, 1394, 1]

print(random_numbers[0])


# 3. Create a program that will only print out the odd numbers in this list. 

# HINT- part of solving this is that you will need to use the range() function. 

number_list= [1,2,3,4,5,6,7,8,9,10]

print()

# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

#shopping_cart = ['notebook', 'pens','tape','mousepad']'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.  

# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3
zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']

# find and print index 0
random_numbers = [10,100,12123, 1394, 1]


# 3. Create a program that will only print out the odd numbers in this list. 

# HINT- part of solving this is that you will need to use the range() function. 

number_list= [1,2,3,4,5,6,7,8,9,10]

x= range(1,10,2)
for n in x:
    print(n)


# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

#keywords - we need to use print(), append(), string value, custom function



shopping_cart = ['notebook', 'pens','tape','mousepad']

def  amazon_Cart():

    user_item = input('what are you buying')
    shopping_cart. append(user_item)
    print(shopping_cart)

    amazon_Cart()






# sequence pf serval varibles under one name / variable 
# collection of things/values that use bracket and comes
# store collections of data

# define Python List- a data type that allows for multiole values within 
# one variable



number_list= [1, 101, 10102, 1010]
string_list= ['wade', 'jahmere']


var_list= [number_list, string_list]

print(var_list[1])


# keywords:
# we know we need to use a function



# clues:
# there are differents item
# have a piece of code that will add up all the item prices including the price of a new itme 




# starter code




list_of_items=['apple', 'orange', 'book']

apple_price= 1.00
orange_price= 3.00
book_price= 10.00


#def checkout():
    #new_item_name= input('what else would you like to add to the cart?')
    #new_item_price= float(input('what is the price of the new item?'))
    #list_of_items.append(new_item_name)
    #print(list_of_items)
    #print(apple_price + orange_price + book_price + new_item_price)

#user_response = input('would you like to add another item?')


#if user_response== 'yes':
    
    #uber_Eat_checkout()

#else:

    #print('proceed to check')


mail= 20

def deletedMail():
   subtraction_number= 5
   remaining_mail = mail-subtraction_number
   print(remaining_mail)


   deletedMail()

    #if mail < 21:  
    
     #deletedMail()

    #else:
        #print('mailbox full')

list_numbers=[1,2,3,4,5,6]
     
def multiplier():
    list_numbers=[1,2,3,4,5,6]      
    for n in list_numbers:
        print(n*3)

        multiplier()








    






